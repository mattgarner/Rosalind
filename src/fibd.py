'''
Created on 19 Mar 2015

@author: matt

Given: Positive integers n <= 100 and m <= 20.

Return: The total number of pairs of rabbits that will remain after the n-th month
if all rabbits live for m months.
'''
import __main__

def fibd(input_filepath):
    input_file = open(input_filepath, "r")
    input = input_file.readline()
    n, m = input.split()
    print "m %d" % m
    print "n %d" % n

if __name__ == __main__:
    fibd()