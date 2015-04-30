'''
Created on 19 Mar 2015

@author: matt

Given: Positive integers n <= 100 and m <= 20.

Return: The total number of pairs of rabbits that will remain after the n-th month
if all rabbits live for m months.

Rabbit pairs produce one infant pair during each month they are adults.
'''

import sys

input_filepath = sys.argv[1]

def fibd(input_filepath):
    input_file = open(input_filepath, "r")
    input_data = input_file.readline()
    n, m = input_data.split()
    print "m(ortality) %s" % m
    print "n(umber of months) %s" % n

    # Initialise - month 1
    age_count = [0] * int(m)
    last_month = list(age_count)
    last_month[0] = 1
    this_month = [None] * int(m)

    # Iterate - months 2 - n
    for month in range(1, int(n)):
        # newborns
        this_month[0] = sum(last_month[1:int(m)])
        # aging adults
        for i in range(1, int(m)):
            this_month[i] = last_month[i-1]
        print this_month
        last_month = list(this_month)

    # Result
    total_alive = sum(last_month)
    print "Total %d" % total_alive

    output_file = open(input_filepath+".results", "w")
    output_file.write(str(total_alive))

if __name__ == '__main__':
    fibd(sys.argv[1])
