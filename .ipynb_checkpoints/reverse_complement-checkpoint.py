#!/usr/bin/env python

""" Finding the reverse complement of a DNA strand """

__author__ = "Navami Shenoy"


def reverse_complement(string):
    reversed_string = string[::-1]  # reverse the string
    rev_comp_string = ''
    
    base_complement = {'A':'T', 'T':'A', 
                        'G':'C', 'C':'G'}
    # find the complement of the reversed string
    for base in reversed_string:
        rev_comp_string = rev_comp_string + base_complement[base]

    return rev_comp_string 


# testing
print(reverse_complement('AAAACCCGGT'))
# Output: ACCGGGTTTT

