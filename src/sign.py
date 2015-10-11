'''
Created on 11 Oct 2015

@author: matt

Given: A positive integer n <=6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
'''

# We will recycle the code from perm, by add an additional step to add all sign permutations to each numerical permutation

import sys
import os
from math import factorial

def read_input(input_filepath):

    input_file = open(input_filepath, "r")
    input_int = int(input_file.readline().strip())
    int_range = range(1, input_int+1)
    return int_range

def next_perm(current_perm):
    # Finds the next permutation using lexicographical ordering algorithm

    # Find the largest index k
    k = -1
    for idx in reversed(range(0,len(current_perm)-1)):
        # such that a[k] < a[k + 1]
        if current_perm[idx] < current_perm[idx+1]:
            k = idx
            break
    # If nothing matched this is the last permutation
    if k == -1:
        return False

    # Find the largest index l greater than k
    indexes = reversed(range(k+1, len(current_perm[k+1:])+k+1))
    l = -1
    for idx in indexes:
        # such that a[k] < a[l]
        if current_perm[k] < current_perm[idx]:
            l = idx
            break


    # Swap a[k] with a[l]
    current_perm[k], current_perm[l] = current_perm[l], current_perm[k]

    # Reverse seq from a[k+1] to a[n]
    current_perm[k+1:] = reversed(current_perm[k+1:])
    return current_perm

def num_perm(int_range):
    input_int = int_range[-1]
    current_perm = int_range

    # Generate all permutations in required format
    perm_count = 1
    permutations = [int_range[:]]

    while next_perm(int_range):
        permutations.append(int_range[:])
        perm_count += 1

    assert perm_count == factorial(input_int), "Error: unexpected number of permutations\n\
                                                Obs: %d\n\
                                                Exp: %d\n"\
                                                % (perm_count, factorial(input_int))

    return permutations

def sign_perm(unsigned_perms):
    # Write a function to generate sign permutations
    # of a set of numerical permutations
    pass


def main(input_filepath):
    int_range = read_input(input_filepath)
    unsigned_perms = num_perm(int_range)


if __name__ == "__main__":
    main(sys.argv[1])

