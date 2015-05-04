'''
Created on 4 May 2015

@author: matt

Given: Six positive integers, each of which does not exceed 20,000.
The integers correspond to the number of couples in a population possessing
each genotype pairing for a given factor. In order, the six given integers
represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in
the next generation, under the assumption that every couple has exactly two
offspring.

'''

import sys


def iev(input_filepath):

    # Setup
    input_file = open(input_filepath, "r")
    population = input_file.readline().split()

    # Expected freq of offspring with dom phenotype
    expected = [2,2,2,1.5,1,0]

    offspring = 0

    # Calculate offspring from each genotype pair
    for pop, exp in zip(population, expected):
        print pop, exp
        offspring += float(pop) * exp
    print "Offspring; ", offspring

    output_file = open(input_filepath+".result", "w")
    output_file.write(str(offspring))
    output_file.close()

if __name__ == "__main__":
    iev(sys.argv[1])