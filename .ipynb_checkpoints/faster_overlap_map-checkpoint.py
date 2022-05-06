#!/usr/bin/env python

""" Assembly problem: Finding all overlapping pairs of sequencing reads  """

__author__ = "Navami Shenoy"


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


# testing
reads = ['CGTACG', 'TACGTA', 'GTACGT', 'ACGTAC', 'GTACGA', 'TACGAT']
overlap_all_pairs(reads,3)
# Output: 
# {('CGTACG', 'TACGTA'): 4,
# ('CGTACG', 'GTACGT'): 5,
# ('CGTACG', 'GTACGA'): 5,
# ('CGTACG', 'TACGAT'): 4,
# ('TACGTA', 'ACGTAC'): 5,
# ('TACGTA', 'CGTACG'): 4,
# ('GTACGT', 'TACGTA'): 5,
# ('GTACGT', 'ACGTAC'): 4,
# ('ACGTAC', 'GTACGT'): 4,
# ('ACGTAC', 'CGTACG'): 5,
# ('ACGTAC', 'GTACGA'): 4,
# ('GTACGA', 'TACGAT'): 5}