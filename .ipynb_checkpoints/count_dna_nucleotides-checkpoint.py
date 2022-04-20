#!/usr/bin/env python

""" Function for counting DNA nucleotides present in a DNA sequences"""

__author__ = "Navami Shenoy"


def countBases(string):
    # counts the number of each A's, C's, G's, and T's in a string
    # returns a list of counts 
    bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in string:
        if char in bases:
            bases[char] += 1
    return list(bases.values())

# testing
# prints the result as numbers separated by spaces 
print(' '.join(str(count) for count in countBases('ACTTG')))
# Output: 1 1 1 2