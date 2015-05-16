'''
Created on 12 May 2015

@author: matt

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could
have been translated, modulo 1,000,000. (Don't neglect the importance of the 
stop codon in protein translation.)

'''
import sys
from twisted.test.test_amp import TotallyDumbProtocol


def mrna(input_filepath):
    # dict of number of codons per aa
    codon_count = {"F": 2, "L": 6, "I": 3, "M": 1,"V": 4, "S": 6, "P": 4, "T": 4, "A": 4, "Y": 2, "H": 2, "Q": 2, "N": 2, "K": 2, "D": 2, "E": 2, "C": 2, "X": 3,  "W": 1, "R": 6, "G": 4}
    assert sum(codon_count.values()) == 64

    input_file = open(input_filepath, "r")
    protein_seq = input_file.readline().strip()

    permutations = []
    for amino_acid in protein_seq:
        permutations.append(codon_count[amino_acid])

    # calculate nucleotide permutations for protein
    total = codon_count["X"]
    millions = 0
    for item in permutations:
        total = total * item
        # prevents the number in total
        # from approaching the old python int memory limit
        while total > 1000000:
            millions +=1
            total = total - 1000000
    print total

    # write results file
    output_file = open(input_filepath + ".result", "w")
    output_file.write(str(total))

if __name__ == "__main__":
    mrna(sys.argv[1])