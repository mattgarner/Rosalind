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

from sys import argv, exit

def get_data(input_filepath):
    with open(input_filepath, "r") as fasta_file:
        fasta_reads = fasta_seqs_to_list(fasta_file)
        return fasta_reads


def fasta_seqs_to_list(fasta_file):
    fasta_index = -1
    fasta_reads = []
    for line in fasta_file:
        if line.startswith(">"):
            fasta_index += 1
            fasta_reads.append("")
        else:
            fasta_reads[fasta_index] += line.strip()
    return fasta_reads


def rev_comp(sequence):
    nucleotide_pair = {"A":"T","T":"A","C":"G","G":"C"}
    complement = ""
    for nucleotide in sequence:
        complement += nucleotide_pair[nucleotide]
    return complement[::-1]


def categorise_reads(fasta_reads):
    '''
    Categorise reads into matched or mismatched within the self set
    '''
    reads = fasta_reads[:]
    matched_reads = []
    mismatched_reads = []

    while reads:
        read = reads.pop()
        # Test for presence of dupe/rev comp of read in remaining reads
        # If found, remove all instances of it from the set of reads
        # Else if not found, record as a mismatch
        if (read in reads) or (rev_comp(read) in reads):
            exclusion_list = [read, rev_comp(read)]
            reads = [i for i in reads if i not in exclusion_list]
            matched_reads.append(read)
        else:
            mismatched_reads.append(read)
    return matched_reads, mismatched_reads


def hamming(query, template):
    '''
    Get the Hamming dist between two seqs
    '''
    hamm_dist = sum([q != t for (q, t) in zip(query, template)])
    return hamm_dist


def get_corrections(all_correct_reads, error_reads):
    corrections = {}
    for error_read in error_reads:
        new_read = find_match(error_read, all_correct_reads, 1)
        if new_read:
            corrections[error_read] = new_read
        else:
            print "Error: Match not found for ", error_read, "in \n", all_correct_reads
            exit()
    return corrections


def find_match(sequence, correct_reads, distance):
    '''
    Find a read within correct reads with the specified Hamming distance from the sequence
    '''
    for read in correct_reads:
        if hamming(sequence, read) == distance:
            return read


def write_results(results, filepath):
    with open(filepath + ".results", "w") as output_file:
        newline = ""
        for item in results.items():
            line = newline + item[0] + "->" + item[1]
            output_file.write(line)
            print line
            newline = "\n"


def corr(input_filepath):
    fasta_reads = get_data(input_filepath)
    correct_reads, error_reads = categorise_reads(fasta_reads)
    all_correct_reads = [rev_comp(read) for read in correct_reads] + correct_reads
    corrections = get_corrections(all_correct_reads, error_reads)
    write_results(corrections, input_filepath)


if __name__ == "__main__":
    corr(argv[1])