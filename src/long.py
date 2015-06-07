'''
Created on 7 Jun 2015

@author: matt

Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
'''

import sys
import os


def get_ends(start_read, end_read):
    start_substr_length = (len(start_read)/2)+1
    end_substr_length = (len(end_read)/2)+1
    ss_start = start_read[0:start_substr_length]
    ss_end = end_read[-end_substr_length:]
    return ss_start, ss_end


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


def assemble_reads(fasta_reads, verbose=False):

    # Take the first read to seed the assembly
    superstring = fasta_reads.pop()

    # To track reads present at each end, since reads overlap each other by len/2 +1.
    # Read len may vary therefore overlap criteria may vary. Tracking reads at ends
    # allows appropriate dynamic overlap length according to current end read.
    current_start_read = superstring
    current_end_read = superstring

    # Assembly loop

    while fasta_reads:
        # Determine sequences at ends to be searched for in reads
        substr_start, substr_end = get_ends(current_start_read, current_end_read)

        if verbose:
            print "Building substrs"
            print "Start: %s\tEnd: %s" % (substr_start, substr_end)

        # Searching each read for presence of  start or end substrings
        # When a match is found the superstring is extended in the appropriate
        # direction by the sequence of the read minus the overlap with the
        # target substring already present in the superstring. The read is 
        # then removed from the pool of reads to be searched.

        for read in fasta_reads:
            # Handle matches at the start of the superstring
            if substr_start in read:
                overlap_pos = read.index(substr_start)
                if verbose:
                    print "StartMatch: "
                    print read
                    print overlap_pos*" " + substr_start
                    print " " * overlap_pos + superstring
                superstring = read[0:overlap_pos] + superstring
                if verbose:
                    print superstring, "\n"
                current_start_read = read
                fasta_reads.remove(read)
                #raw_input()
                break

            # Handle matches at the end of the superstring
            if substr_end in read:
                overlap_pos = read.index(substr_end)
                if verbose:
                    print "End Match: "
                    print " " * (overlap_pos + len(substr_end)) + substr_end
                    print " " * len(substr_end) + read
                    print superstring
                superstring = superstring + read[overlap_pos+len(substr_end):]
                if verbose:
                    print superstring, "\n"
                current_end_read = read
                fasta_reads.remove(read)
                #raw_input()
                break

    print superstring
    return superstring


def long(input_filepath):
    verbose = True
    assert os.path.exists(input_filepath), "Error: File not found!"
    with open(input_filepath, "r") as fasta_file:

        # Get reads into list
        fasta_reads = fasta_seqs_to_list(fasta_file)
        assert len(fasta_reads) > 0, "Error: no reads extracted"

        # Assemble reads
        assembly = assemble_reads(fasta_reads)
        assert len(assembly) > 0, "Error: assembly of reads failed"

        with open(input_filepath+".result", "w") as output_file:
            output_file.write(assembly)

if __name__ == "__main__":
    long(sys.argv[1])