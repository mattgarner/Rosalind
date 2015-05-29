'''
Created on 27 May 2015

@author: matt

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
'''

import sys

def revp(input_filepath):


    complement = {"A":"T","T":"A","C":"G","G":"C"}
    input_file = open(input_filepath, "r")
    sequence = ""

    # Get sequence from fasta
    for line in input_file:
        if not line.startswith(">"):
            sequence = sequence + line.strip()

    results = []
    # Find palindrome seeds in sequence with space to expand to len 4
    for position in range(1, len(sequence)-2):
        if complement[sequence[position]] == sequence[position+1]:

            # Expand to find palindromes on len >= 4, staying within sequence bounds
            extension = 1
            while position-extension >= 0\
            and position+1+extension < len(sequence)\
            and complement[sequence[position-extension]] == sequence[position+1+extension]:
                start_pos = position-extension+1
                end_pos = position+extension+2
                length = end_pos-start_pos+1

                if length <= 12:
                    results.append([start_pos, length])
                extension +=1

    output_file = open(input_filepath+".result", "w")
    output_str = ""
    for result in results:
        output_str += (str(result[0]) + " " + str(result[1]) + "\n")
    output_file.write(output_str.strip())

if __name__ == "__main__":
    revp(sys.argv[1])