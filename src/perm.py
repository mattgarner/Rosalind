'''
Created on 18 May 2015

@author: matt

Given: A positive integer n<=7.

Return: The total number of permutations of length n,
followed by a list of all such permutations (in any order).
'''

import sys
import os
from math import factorial


def perm(input_filepath):

    assert os.path.exists(input_filepath), "Error: file not found"
    input_file = open(input_filepath, "r")
    input_int = int(input_file.read().strip())
    int_range = range(1, input_int+1)
    print int_range

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
            if int_range[k] < current_perm[idx]:
                l = idx
                break


        # Swap a[k] with a[l]
        current_perm[k], current_perm[l] = current_perm[l], current_perm[k]

        # Reverse seq from a[k+1] to a[n]
        current_perm[k+1:] = reversed(current_perm[k+1:])
        print current_perm
        return True


    # First row of results contains 1..n

    result_str = ""
    for value in int_range:
            result_str += str(value) + " "
    result_str = result_str.strip() + "\n"

    # Generate all permutations in required format
    perm_count = 1
    while next_perm(int_range):
        for value in int_range:
            result_str += str(value) + " "
        result_str = result_str.strip() + "\n"
        perm_count += 1
    assert perm_count == factorial(input_int), "Error: unexpected number of permutations\n\
                                                Obs: %d\n\
                                                Exp: %d\n"\
                                                % (perm_count, factorial(input_int))

    # First row of results file contains number of permutations
    result_str = str(perm_count) + "\n" + result_str

    # Write to results file
    print result_str
    output_file = open(input_filepath + ".result", "w")
    output_file.write(result_str.strip())
    output_file.close()
    
if __name__ == "__main__":
    perm(sys.argv[1])