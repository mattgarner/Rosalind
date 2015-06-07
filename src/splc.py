'''
Created on 29 May 2015

@author: matt

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons
of s. (Note: Only one solution will exist for the dataset provided.)
'''

import sys
import os

def splc(input_filepath):
    fasta_seqs = []
    i = -1
    assert os.path.exists(input_filepath), "Error: File not found"
    with open(input_filepath, "r") as input_file:
        # Parse fasta
        for line in input_file:
            if not line.startswith(">"):
                try:
                    fasta_seqs[i] += line.strip()
                except:
                    fasta_seqs.append(line.strip())
            else:
                i += 1
    
    # Remove introns
    cDNA = fasta_seqs[0]
    for intron in fasta_seqs[1:]:
        cDNA = cDNA.replace(intron, "")

    # Set up codon table
    nucleotides = ["T", "C", "A", "G"]
    codons = [a+b+c
              for a in nucleotides
              for b in nucleotides
              for c in nucleotides]
    aacids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codontable = dict(zip(codons, aacids))

    # Find start codon
    start_codon_index = cDNA.find("ATG")

    # Generate list of codon seqs
    codonlist = [cDNA[i:i+3] for i in range(start_codon_index, len(cDNA), 3)]
    protein = ""

    # Translate
    for c in codonlist:
        if len(c) == 3:
            if codontable[c] == "*":
                break
            else:
                protein += codontable[c]

    print protein

    with open(input_filepath+".result", "w") as output_file:
        output_file.write(protein)

if __name__ == "__main__":
    splc(sys.argv[1])