'''
Created on 11 Oct 2015

@author: matt

Given: A collection of at most 10 symbols defining an ordered alphabet,
and a positive integer n (n<=10).

Return: All strings of length n that can be formed from the alphabet,
ordered lexicographically.
'''

# Max number of expected kmers is 10 **10 = 10000000000
# Each kmer is up to 10 chars long
# This is too large to store in memory
# Therefore need to generate kmers in lexicographical order,
# rather than generate then sort
# Note that the lexicographical order is defined in the input,
# not by the standard order


# Need to generate i.e AAAA, AAAC, AAAG, AAAT
#                      AACA, AACC, AACG, AACT
#                      AATA, AATC, AATG, AATT
#                      AAGA, AAGC, AAGG, AAGT


import sys
import os


def get_data(input_filepath):
    '''
    Read the input file and return data in variables
    '''
    with open(input_filepath) as input_file:
        alphabet = input_file.readline()
        alphabet = [char for char in alphabet if char not in ("\n", " ")]
        print "Alphabet: %s" % alphabet

        kmer_len = input_file.readline()
        kmer_len.strip
        kmer_len = int(kmer_len)
        print "Kmer length: %d" % kmer_len
        return alphabet, kmer_len


def generate_kmers2(alphabet, kmer_len, input_filepath):
    '''
    Generate the kmers in lexicographical order, and write to output file
    '''

    # Easier to index using base matching number of chars in alphabet
    base = len(alphabet)
    # Starts with [0 ,0, 0, ..., 0]
    kmers_index = [int("0", base)]*kmer_len
    kmer_buffer = []
    max_buffer_length = 1000000
    total_combos = base**kmer_len

    i = 1
    while i <= total_combos:
        # Get kmer for current index
        kmer = [alphabet[index] for index in kmers_index]
        kmer_buffer.append("".join(kmer))

        # Purge buffer
        if (len(kmer_buffer) == max_buffer_length) or (i == total_combos):
            #print "Purging kmer buffer..."
            write_outfile(input_filepath, kmer_buffer)
            #print "Purging complete!"
            print "%.2f%% complete" % (float(i)/total_combos * 100)
            kmer_buffer = []

        # Increment index(es)
        kmers_index[-1] = (kmers_index[-1] + 1) % base
        if kmers_index[-1] % base == 0:
            for index in reversed(range(0, len(kmers_index)-1)):
                if kmers_index[index+1] == 0:
                    kmers_index[index] = (kmers_index[index] + 1) % base
                else:
                    break
        i += 1

def sort_kmers(kmers):
    return kmers.sort()


def write_outfile(input_filepath, kmers):
        output_file = open(input_filepath + ".results", "w")
        for kmer in kmers:
            output_file.write(kmer + "\n")


def lexf(input_filepath):
    print "\nInput:"
    alphabet, kmer_len = get_data(input_filepath)
    print "\nGenerating kmers..."
    generate_kmers2(alphabet, kmer_len, input_filepath)
    #print "Total kmers: %d" % len(kmers)
    #print "Alphabet length ** kmer length = %d" % len(alphabet)**kmer_len

    #print "\nSorting kmers..."
    #sorted_kmers = kmers.sort()
    #if kmers == sorted_kmers:
    #    print "SAME"
    #print "Sorting complete!"

if __name__ == "__main__":
    lexf(sys.argv[1])