#!/usr/bin/env python

""" Assembly problem: Finding all overlapping pairs of sequencing reads  """

__author__ = "Navami Shenoy"

# download the file
import wget
from itertools import permutations

wget.download("https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/ads1_week4_reads.fq", "ads1_week4_reads.fq")


def readFASTQ(filename):
    sequences = []
    qualities = []
    with open(filename) as f:
        while True:
            f.readline()  # reads the 1st line. We don't need this info
            seq = f.readline().rstrip() # this is the second line. it has the sequence we want
            f.readline()  #reads the 3rd line, which is just a '+'
            qual = f.readline().rstrip()  #reads the base qualities line
            
            if len(seq) == 0:  #if we have reached the end of the file, seq would be initialized as empty
                break
                
            sequences.append(seq) # if we haven't reached the end, then we want to append the seq and qual values to our list
            qualities.append(qual)
            
    return sequences, qualities

# helper function
def overlap(a,b, min_length = 3): 
    """ calculates the overlap length between two strings a and b. 
        Author: Ben Langmead, Johns Hopkins University, Baltimore, MD """
    start = 0
    
    while True:
        # find the prefix of b in a
        start = a.find(b[:min_length],start) 
        if start == -1: 
            # there is no overlap :(
            return 0  
        if b.startswith(a[start:]): 
            return len(a) - start  
        start += 1 


        
# faster version of naive_overlap_graph.py
def overlap_all_pairs(reads, k): # k = minimum overlap length
    """ finds all pairs of reads that have an overlap of 
        of a given length. returns an overlap map in the
        form of a dictionary """
    kmers = {}
    overlaps = {}
    # go through each read and break it down into k-mers:   
    for read in reads:
        for i in range(len(read)-k+1):
            # store all reads that contain the k-mer as 
            # the k-mer's value in the dictionary:
            kmers.setdefault(read[i:i+k], set()).add(read)
    
  
    for read in reads:
        # if the k-length suffix of a read matches 
        # a k-mer in the k-mer dictionary:
        if read[-k:] in kmers:
            # get all the reads that contain the k-mer
            reads_list = kmers[read[-k:]]
            # calculate overlap length between the given 
            # read and all the reads that contain the k-mer:
            for kmer_read in reads_list:
                overlap_length = overlap(read, kmer_read, min_length=k)
                # ignore cases where the reads are made of the 
                # same exact sequence; if an overlap exists: 
                if read != kmer_read and overlap_length != 0:
                    # add the pairs and theor overlap length to the dictionary:
                    overlaps[(read,kmer_read)] = overlap_length
                
    return overlaps



def scs(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length """
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup  # found shorter superstring
    return shortest_sup  # return shortest


def shortest_superstring(overlaps):
    shortest_sup = None
    superstring = ''
    for key,value in overlaps.items():
        superstring += key[1][value:]
    if shortest_sup is None or len(superstring) < len(shortest_sup):
        shortest_sup = superstring
    return shortest_sup



#testing
reads = ['CGTACG', 'TACGTA', 'GTACGT', 'ACGTAC', 'GTACGA', 'TACGAT']
overlaps = overlap_all_pairs(reads,3)
print(shortest_superstring(overlaps))
print(overlaps)