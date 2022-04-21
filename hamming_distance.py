#!/usr/bin/env python

""" Counting point mutations: finding the Hamming distance
    between two strings of the same length, X and Y """

__author__ = "Navami Shenoy"


def hammingDistance(x,y):
    """ computes the number of mismatches between 
        two strings of equal length, x and y """
    # number of substitutions needed to make 
    #x exactly the same as y:
    num_subs = 0
    if len(x) == len(y):
        for i in range(0,len(x)):
            if not x[i] == y[i]:
                num_subs += 1
                
    return num_subs


# testing
x = 'GAGCCTACTAACGGGAT'
y = 'CATCGTAATGACGGCCT'
hammingDistance(x,y)
# Output: 7