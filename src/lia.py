'''
Created on 4 May 2015

@author: matt

Given: Two positive integers k (k<=7) and N (N<=2^k). 
In this problem, we begin with Tom, who in the 0th generation
has genotype Aa Bb. Tom has two children in the 1st generation,
each of whom has two children, and so on. Each organism always
mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will
belong to the k-th generation of Tom's family tree
(don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.
'''

import os
import sys

def lia(input_filepath):
    input_file = open(input_filepath, "r")
    k, N = input_file.readline().split()
    total_offspring = 2**int(k)
    print "Total offspring: %s" % total_offspring
    AaBb_odds = (0.25 * 0.75) + (0.75 * 0.25) + (0.25 * 0.25)
    print "AaBb odds: %d" % float(AaBb_odds)
    total_AaBb = 2 * 0.25 * total_offspring
    print "Total double hets: %s" % int(total_AaBb)

if __name__ == "__main__":
    lia(sys.argv[1])