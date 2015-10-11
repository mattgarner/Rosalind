'''
Created on 7 Jun 2015

@author: matt

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in
FASTA format. Some of these reads were generated with a single-nucleotide error.
For each read s in the dataset, one of the following applies:

    s was correctly sequenced and appears in the dataset at least twice
    (possibly as a reverse complement);

    s is incorrect, it appears in the dataset exactly once,
    and its Hamming distance is 1 with respect to exactly one correct read in 
    the dataset (or its reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]".
(Each correction must be a single symbol substitution,
and you may return the corrections in any order.)

'''
import os
import sys
from fibd import input_filepath

def fasta_seqs_to_list(fasta_file):
    fasta_index = -1
    fasta_reads = []
    for line in fasta_file:
        if line.startswith(">"):
            fasta_index += 1
            fasta_reads.append("")
        else:
            fasta_reads[fasta_index] += line.strip()

    print "reads:"
    for read in fasta_reads:
        print read
    return fasta_reads

def rev_comp(sequence):
    nucleotide_pair = {"A":"T","T":"A","C":"G","G":"C"}
    complement = ""
    for nucleotide in sequence:
        complement += nucleotide_pair[nucleotide]
    return complement[::-1]

def mismatched_reads(fasta_reads):
    mismatches = []
    # To be cleaned up later, avoids strange behaviour in mismatched reads if
    # fasta_reads is used. Elements of list are modified in a way I don't yet
    # understand
    reads = fasta_reads[:]
    while reads:
        read = reads.pop()
        print "read:", read
        print "reads\n", reads
        # Test for presence of dupe/rev comp of read in remaining reads
        # If found, remove all instances of it from the set of reads
        # Else if not found, record as a mismatch
        if (read in reads) or (rev_comp(read) in reads):
            print "Match found for %s" % read
            print reads, "\n"
            exclusion_list = [read, rev_comp(read)]
            reads = [i for i in reads if i not in exclusion_list]
            print reads, "\n"
        else:
            print "Not found %s\n" % read
            print reads
            mismatches.append(read)
        raw_input()
    return mismatches

def corr(input_filepath):
    with open(input_filepath, "r") as fasta_file:
        fasta_reads = fasta_seqs_to_list(fasta_file)
    errors = mismatched_reads(fasta_reads)
    print "Reads", fasta_reads
    print "Errors", errors
    # Search fasta_reads for matches with Hamming distance of 1

if __name__ == "__main__":
    corr(sys.argv[1])