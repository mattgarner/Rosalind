'''
Created on 18 Jun 2015

@author: matt


Given: A positive integer n<=10000 followed by a permutation p of length n.

Return: A longest increasing subsequence of p,
followed by a longest decreasing subsequence of p.
'''

import sys

def lgis(input_filepath):

    def get_input(input_filepath):
        with open(input_filepath, "r") as input_file:
            n = input_file.readline()
            n = n.strip()
            print n

            permutation = input_file.readline()
            permutation = [char for char in permutation.rstrip() if char != " "]
            print permutation

        return n, permutation

    def longest_incr(permutation):
        for pos, num in permutation:
            # need to stop if current > remaining possible

            print



    n, permutation = get_input(input_filepath)
    longest_inc_subseq = longest_incr(permutation)


if __name__ == "__main__":
    lgis(sys.argv[1])