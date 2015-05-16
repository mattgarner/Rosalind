'''
Created on 14 May 2015

@author: matt

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif,
output its given access ID followed by a list of locations in
the protein string where the motif can be found.

'''

import sys
import urllib2
import re

def mprt(input_filepath, motif = "N{P}[ST]{P}"):

    def input2uniprotids(filepath):
        input_file = open(input_filepath, "r")
        uniprot_ids = []
        for line in input_file:
            uniprot_ids.append(line.strip())
        return uniprot_ids

    def uniprotid2fastaseq(uniprot_id):
            url = "http://www.uniprot.org/uniprot/%s.fasta" % uniprot_id
            source = urllib2.urlopen(url)
            fasta_data = source.read()
            fasta_lines = fasta_data.strip().split("\n")
            fasta_seq = ""
            for line in fasta_lines:
                if line[0] != ">":
                    fasta_seq += line
            return fasta_seq

    def parse_motif(motif):

        motif_components = []
        motif_len = len(motif)-1
        i = 0

        # break down motif into motif_components
        while i < motif_len:
            delimiters = {"{": "}", "[": "]"}

            # to handle NOT{}/OR[] blocks
            if motif[i] in delimiters.keys():
                start = i
                end = motif[i+1:].find(delimiters[motif[i]])+i+1
                component = motif[start:end+1]
                motif_components.append(component)
                i = i+len(component)

            # to handle IS blocks
            else:
                component = motif[i]
                motif_components.append(component)
                i += len(component)

        return motif_components

    def motif_regex(motif_components):
        regex_pattern = ""
        for idx, component in enumerate(motif_components):
            component_pattern = ""
            print idx
            if idx == 1:
                component_pattern += "(?="
            # is not
            if component[0] == "{":
                component_pattern += "[^" + component[1:-1] + "]"

            # is OR
            elif component[0] == "[":
                component_pattern += component

            # is
            else:
                component_pattern += "[" + component + "]"

            regex_pattern += component_pattern
        regex_pattern += ")"

        regex = re.compile(regex_pattern)
        return regex

    def index_matches(string, regex):
        match_indexes = []
        match_objects = regex.finditer(string)
        for match in match_objects:
            match_indexes.append(match.start())
        return match_indexes

    # Break motif into components

    
    motif_components = parse_motif(motif)
    # Use components to compile regex to match motif
    regex = motif_regex(motif_components)

    # Extract uniprot ids from input file
    uniprot_ids = input2uniprotids(input_filepath)
    results = {}

    for id in uniprot_ids:
        # Get fasta sequence for uniprot id
        uniprot_seq = uniprotid2fastaseq(id)

        # get indexes of motif within sequence
        motif_indexes = index_matches(uniprot_seq, regex)

        # if motif was found in sequence store result
        if motif_indexes:
            results[id] = motif_indexes

    # write results to the output file
    output_file = open(input_filepath + ".results", "w")
    output = ""
    # keeping the order the same
    for id in uniprot_ids:
        # if any matches were found in a sequence, write the result
        # in the format required
        if id in results.keys():
            output += id + "\n"
            for motif_index in results[id]:
                output += str(motif_index+1) + " "
            output = output.strip()  # Remove trailing space from last index
            output += "\n"
    output = output.strip()  # Remove trailing "\n from last line
    print output
    output_file.write(output)


if __name__ == "__main__":
    mprt(sys.argv[1])