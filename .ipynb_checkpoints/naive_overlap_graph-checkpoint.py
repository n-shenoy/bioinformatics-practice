#!/usr/bin/env python

""" Creating an overlap graph of sequencing reads with a 
    pre-specified length of overlap """

__author__ = "Navami Shenoy"


from itertools import permutations as pm

def readFASTA(filename):
    """ read and parse FASTA file. capture 
        labels and their corresponding sequences
        in a dictionary """ 
    # works more like parsing a FASTQ file
    seqs = {}
    with open(filename, 'r') as f:    
        for line in f:
            if line[0] == '>': # capture label
                label = line[1:].rstrip()
                genome = ''
            else:    # capture sequence
                genome += line.rstrip() 
                seqs[label] = genome
    return seqs


# test file, source: https://rosalind.info
file = 'rosalind_overlap_graph.txt' 
reads = readFASTA(file)


def naive_overlap_graph(reads, k):
    """ returns a list containing sequences that
        have an overlap length of k """
    overlap_seqs = []
    labels = list(reads.keys()) 
    strings = list(reads.values())
    start = 0 
    
    # for every permutation of the sequences in dictionary
    for string1, string2 in pm(strings,2): 
        # if suffix of string 1 matches the prefix of string 2,
        # store the labels corresponding to strings 1 and 2 as a  
        # tuple in the overlap_seqs list:
        if string1[len(string1)-k:] == string2[:k] and string1 != string2:
            key = labels[strings.index(string1)]
            value = labels[strings.index(string2)]
            overlap_seqs.append((key,value))
            
    return overlap_seqs
            
            
        
# testing 
overlaps = naive_overlap_graph(reads,3) # overlap length = 3
for element in overlaps: # print each value in the tuple side-by-side
    print(element[0],element[1])
# Output is an adjacency list containing label names
# of two strings with an overlap length of 3. For example:
#   Rosalind_6569 Rosalind_5735
#   Rosalind_5716 Rosalind_4612
#   Rosalind_3354 Rosalind_0189
#   Rosalind_3354 Rosalind_2686....
# ....and so on.    
        
# (for instance, the first output line means that the 
# suffix of length 3 of the string in Rosalind_6569
# matches the prefix of length 3 of the string labeled 
# Rosalind_4612)

    
    