'''
Created on 4 May 2015

@author: matt

Given: A collection of k (k<=100) DNA strings of length
at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection.
(If multiple solutions exist, you may return any single solution.)
'''

import sys
import os
from __builtin__ import reversed


def lcsm(input_filepath):
    
    assert os.path.exists(input_filepath), "Error: input file does not exist"
    input_file = open(input_filepath, "r")

    # Get fasta headers/sequences
    fasta_records = {}
    for line in input_file:
        line = line.strip()
        if line.startswith(">"):
            record_header = line
            fasta_records[line] = ""
        else:
            fasta_records[record_header] += line

    # start with shortest seq, since common seq must be found in all seqs
    shortest_seq = min(fasta_records.values(), key=len)
    sequence_length = len(shortest_seq)

    # loop through all substrings searching for largest hit in all seqs
    offset = 0
    for substring_length in list(reversed(range(1, sequence_length+1))):
        for offset in range(0, sequence_length - substring_length+1):
            substring = shortest_seq[offset:substring_length+offset]
            if all(substring in i for i in fasta_records.values()):
                output_file = open(input_filepath+".result", "w")
                output_file.write(substring)
                output_file.close()
                print "Results written to %s" % input_filepath + ".result"
                return

if __name__ == "__main__":
    lcsm(sys.argv[1])