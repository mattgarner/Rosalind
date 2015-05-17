'''
Created on 16 May 2015

@author: matt

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
'''

import sys
import os
import re


def orf(input_filepath):

    def fasta_seq(input_filepath):

        assert os.path.exists(input_filepath),\
            "Error: file %s not found" % input_filepath
        fasta_file = open(input_filepath, "r")

        # Place fasta seqeunces in a dict {header:sequence}
        sequences = {}
        for line in fasta_file:
            line = line.strip("\n")
            if line[0] == ">":
                header = line[1:]
                sequences[header] = ""
            else:
                sequences[header] += line

        assert len(sequences) > 0,\
            "Error: no sequences found in %s" % input_filepath
        return sequences

    def reverse_comp(sequence):

        # flip it...
        complement_strand_3to5 = ""
        nucleotide_pairs = {"A": "T",
                            "T": "A",
                            "G": "C",
                            "C": "G"}
        for nucleotide in sequence:
            complement_strand_3to5 += nucleotide_pairs[nucleotide]

        # and reverse it...
            complement_strand_5to3 = complement_strand_3to5[::-1]

        return complement_strand_5to3


    # Get nuc seq, discard header since not required for return

    def get_orf_seqs(sequence):

        # Start codon - any number of non stop codons - stop codon
        orf_search = re.compile("(?=((?P<start_codon>A[T|U]G)(?P<codons>([ATUCG]{3})*?)(?P<stop_codon>[T|U](AG|GA|AA))))")

        orfs = orf_search.finditer(sequence)
        orf_seqs = []

        for orf in orfs:
            orf_seq = orf.group("start_codon") + orf.group("codons")
            orf_seqs.append(orf_seq)

        return orf_seqs

    def DNA_to_prot(sequence):

        #Set up codon table
        nucleotides = ["T","C","A","G"]
        codons = [a+b+c for a in nucleotides for b in nucleotides for c in nucleotides]
        aacids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
        codon_table = dict(zip(codons, aacids))

        #Convert sequence to protein
        protein = ""
        codon_list = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
        for codon in codon_list:
            if len(codon) == 3:
                if codon_table[codon] == "*":
                    break
                else:
                    protein += codon_table[codon]
        print protein
        return protein

    def write_results(results):

        output_file = open(input_filepath+".results", "wa")
        result_string = ""
        for item in results:
            result_string += item + "\n"
        result_string = result_string.strip()
        output_file.write(result_string)

    f_sequence = fasta_seq(input_filepath).values()[0]  # Get fasta seq from file
    # Generate reverse complement from seq
    r_sequence = reverse_comp(f_sequence)
    # Get all ORFs from both seqs
    orf_seqs = []
    for sequence in f_sequence, r_sequence:
        orf_seqs += get_orf_seqs(sequence)
    # Remove duplicates
    orf_seqs = list(set(orf_seqs))
    # Convert to protein sequence
    proteins = []
    for seq in orf_seqs:
        proteins.append(DNA_to_prot(seq))
    # Generate results file
    write_results(proteins)

if __name__ == "__main__":
    orf(sys.argv[1])
