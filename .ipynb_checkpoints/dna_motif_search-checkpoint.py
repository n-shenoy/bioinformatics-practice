#!/usr/bin/env python

""" Finding all occurrences of a motif in a DNA string using K-mer indexing """

__author__ = "Navami Shenoy"


import bisect as bi
   
def createIndex(text, pattern):
    """ creates a kmer index object for the text T """
    k = len(pattern) # divide the text based on the pattern's length
    index = []
    for i in range(0, len(text)-k+1):
        kmer = text[i:i+k]
        position = i + 1 # add 1 to switch to 1-based numbering
        index.append((kmer, position))
    index.sort() # alphabetical order
    return index # positions now start from 1, not 0



def pattern_search(text, pattern, index):
    """ uses binary search to look for an exact match of
        a string in the index created by createIndex() """
    i = bi.bisect_left(index, (pattern, -1))
    positions = []
    while i < len(index):
        if pattern == index[i][0]:
            positions.append(index[i][1])
        i += 1
    return positions 



# testing
t = 'AGCTGGACATTAGGTGGCATGCTCAT' # text
p = 'CAT' # substring
kmerIndex = createIndex(t,p) 
pattern_search(t,p, kmerIndex)
# Output: [8, 18, 24]  

t = 'GATATATGCATATACTT'
p = 'ATAT'
kmerIndex = createIndex(t,p)
pattern_search(t,p, kmerIndex)
# Output: [2, 4, 10]

