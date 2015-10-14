'''
Created on 11 Oct 2015

@author: matt

Given: A positive integer n <=6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
'''

# We will recycle some code from perm, by add an additional step to add all sign permutations to each numerical permutation

import sys
import os
import itertools
from math import factorial


def read_input(input_filepath):
    '''
    Gets data from the input file
    '''
    input_file = open(input_filepath, "r")
    input_int = int(input_file.readline().strip())
    int_range = range(1, input_int+1)
    return int_range

def next_perm(current_perm):
    '''
    Takes a permutations and finds the next permutation using lexicographical ordering algorithm
    '''
    
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
    '''
    Generates all unsigned numerical permutations using next_perm
    '''
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
    '''
    Generates all signed permutations for each unsigned permutation in unsigned_perms
    '''

    perm_len = len(unsigned_perms[0])
    sign_template = list(
        itertools.product([-1, 1], repeat=perm_len))
    assert len(sign_template) == 2**perm_len, "Error: unexpected sign template len"
    signed_perms = []
    for perm in unsigned_perms:
        for signs in sign_template:
            signed_perm = [a*b for a,b in zip(perm, signs)]
            signed_perms.append(signed_perm)
    return signed_perms


def write_result(input_filepath, signed_perms):
    '''
    Write signed perms count and each perm to output
    '''
    with open(input_filepath + ".result", "w") as output_file:
        output_file.write(str(len(signed_perms)) + "\n")
        for perm in signed_perms:
                output_file.write(" ".join((str(x)) for x in perm) + "\n")




def main(input_filepath): 
    int_range = read_input(input_filepath)
    exp_unsigned_perms = factorial(len(int_range))
    print "Expected unsigned perms: ", exp_unsigned_perms
    unsigned_perms = num_perm(int_range)
    print "Observed unsigned perms: ", len(unsigned_perms)
    assert exp_unsigned_perms == len(unsigned_perms), "Error: unexpected number of unsigned permutations"

    exp_signed_perms = exp_unsigned_perms * (2**len(int_range))
    print "\nExpected signed perms: ", exp_signed_perms
    signed_perms = sign_perm(unsigned_perms)
    print "Observed unsigned perms: ", len(signed_perms)
    assert exp_signed_perms == len(signed_perms), "Error: unexpected number of signed permutations"

    write_result(input_filepath, signed_perms)
    print "Complete!"

if __name__ == "__main__":
    main(sys.argv[1])

