'''
Created on 14 Oct 2015

@author: matt


Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
'''


import sys

def tran(input_filepath):


    def get_input(input_filepath):
        with open(input_filepath, "r") as input_file:
            return input_file.readlines()

    def parse_fasta(fasta):
        seqs = {}
        for line in fasta:
            if line.startswith(">"):
                title = line.strip()
                seqs[title] = ""
            else:
                seqs[title] += line.strip()
        return seqs

    def count_ts_tv(seqs):

        # u == pUrine, y = pYrimidine
        base_type = {"A":"u",
                     "T":"y",
                     "C":"y",
                     "G":"u",
                     }

        ts_tv_count = {"transition": 0,
                       "transversion": 0,
                       "match": 0
                       }

        dna_strings = seqs.values()

        for pair in zip(dna_strings[0], dna_strings[1]):
            if (pair[0] == pair[1]):
                ts_tv_count["match"] += 1
            elif (base_type[pair[0]] != base_type[pair[1]]):
                ts_tv_count["transversion"] += 1
            else:
                ts_tv_count["transition"] += 1

        return ts_tv_count

    def get_ts_tv_ratio(trans_count):
        if trans_count["transversion"] == 0:
            ts_tv = "Divide by zero error"
        else:
            ts_tv = float(trans_count["transition"])/trans_count["transversion"]
        return ts_tv


    def write_result(input_filepath, result):
        with open(input_filepath + ".result", "w") as output_file:
            output_file.write(str(result))

    fasta = get_input(input_filepath)
    seqs = parse_fasta(fasta)
    trans_count = count_ts_tv(seqs)
    ts_tv_ratio = get_ts_tv_ratio(trans_count)
    write_result(input_filepath, ts_tv_ratio)
    print "TS/TV = %f" % ts_tv_ratio
    print "Complete!"

if __name__ == "__main__":
    tran(sys.argv[1])