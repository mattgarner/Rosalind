'''
Created on 18 Jun 2015

@author: matt


Given: A positive integer n<=10000 followed by a permutation p of length n.

Return: A longest increasing subsequence of p,
followed by a longest decreasing subsequence of p.
'''

import sys

def lgis(input_filepath):

    with open(input_filepath, "r") as input_file:
        n = input_file.readline()
        n = n.strip("\n")
        print n

        permutation = input_file.readline()
        permutation = [char for char in permutation.rstrip() if char != " "]
        print permutation


if __name__ == "__main__":
    lgis(sys.argv[1])