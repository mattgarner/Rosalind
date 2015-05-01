'''
Created on 1 May 2015

@author: matt
'''

import os
import sys

def grph(input_filepath):
    assert os.path.exists(input_filepath), "Error: %s does not exist" % input_filepath
    input_file = open(input_filepath, "r")

    # Get fasta headers/sequences
    fasta_sequences = {}
    for line in input_file:
        line = line.strip()
        if line.startswith(">"):
            record_header = line
            fasta_sequences[line] = ""
        else:
            fasta_sequences[record_header] += line

    # Search for overlaps
    output_file = open(input_filepath+".results", "w")
    for suff_header, suff_seq in fasta_sequences.items():
        for pref_header, pref_seq in fasta_sequences.items():
            if ((suff_seq != pref_seq) and (suff_seq[-3:] == pref_seq[:3])):
                output_file.write(suff_header[1:] + " " + pref_header[1:] + "\n")

    print "Results written to ", input_filepath + ".results"

if __name__ == "__main__":
    grph(sys.argv[1])