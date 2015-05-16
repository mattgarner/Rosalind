'''
Created on 15 May 2015

@author: matt

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
'''

import sys

def prtn(input_filepath):

    def aa_weight(aa_id):
        aa_weights = {"A": 71.03711,
                      "C": 103.00919,
                      "D": 115.02694,
                      "E": 129.04259,
                      "F": 147.06841,
                      "G": 57.02146,
                      "H": 137.05891,
                      "I": 113.08406,
                      "K": 128.09496,
                      "L": 113.08406,
                      "M": 131.04049,
                      "N": 114.04293,
                      "P": 97.05276,
                      "Q": 128.05858,
                      "R": 156.10111,
                      "S": 87.03203,
                      "T": 101.04768,
                      "V": 99.06841,
                      "W": 186.07931,
                      "Y": 163.06333}
        assert aa_id in aa_weights.keys(),\
            "Error: unknown amino acid %s" % aa_id
        return aa_weights(aa_id)    

    def get_protein_seq(input_filepath):

        input_file = open(input_filepath, "r")
        protein_seq = input_file.readline().strip()
        return protein_seq

    def calc_protein_weight(protein_seq):

        protein_weight = 0
        for amino_acid in protein_seq:
            protein_weight += aa_weight(amino_acid)
        return protein_weight

    def write_results(results, input_filepath):

        output_file = open(input_filepath+".results", "w")
        output_file.write(results)
        output_file.close()

    protein_seq = get_protein_seq(input_filepath)
    protein_weight = calc_protein_weight(protein_seq)
    write_results(protein_weight, input_filepath)

    if __name__ == "__main__":
        prtn(sys.argv[1])