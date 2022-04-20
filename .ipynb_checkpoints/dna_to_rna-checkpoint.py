#!/usr/bin/env python

""" Transcribing a DNA sequence into RNA """

__author__ = "Navami Shenoy"


def dna_to_rna(dna):
    # converts all thymines in the dna sequence to uracils 
    rna = dna 
    for base in rna:
        if base == 'T':
            rna = rna.replace('T','U')
    return rna


# testing
print(dna_to_rna('GTATCAGT'))
# Output: 'GUAUCAGU'

