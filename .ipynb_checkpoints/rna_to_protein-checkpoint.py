#!/usr/bin/env python

""" Translating RNA into an amino acid string """

__author__ = "Navami Shenoy"


def rna_to_protein(rna):
    # converts RNA string into a protein string
    # the keys of this codon dictionary contains only the
    # prefix of the amino acids. this is to save time from
    # searching for every single possible codon in the codon table.
    # this is possible because multiple codons code for the same amino acid,
    # and they usually differ by only the last base 
    codons = {'GC' : 'A', 
              'CG' : 'R', 
              'AG' : {'A':'R', 'G':'R','U':'S', 'C':'S'},
              'AA' : {'U':'N', 'C':'N','A':'K','G':'K'}, 
              'GA' : {'U':'D','C':'D','A':'E','G':'E'},
              'UG' : {'U':'C','C':'C','G':'W','A':''},
              'CA' : {'A':'Q','G':'Q','U':'H','C':'H'},
              'GG' : 'G',
              'AU' : {'U':'I','C':'I','A':'I','G':'M'},
              'CU' : 'L', 
              'UU' : {'A':'L','G':'L','U':'F','C':'F'},
              'CC' : 'P',
              'UC' : 'S',
              'AC' : 'T',
              'UA' : {'U':'Y','C':'Y','A':'','G':''},
              'GU' : 'V',
             }
    
    protein = ''
    i = 0
    while i <= (len(rna)-3):
        # if the codon codes only for one amino acid,
            # simply add the amino acid to the protein string
        if len(codons[rna[i:i+2]]) == 1: # this way, we only compare 2 characters at a time
            protein = protein + codons[rna[i:i+2]]
        
        # if the codon codes for multiple amino acids,
            # look for the amino acid that matches the suffix or the third
            # character of the codon 
        else:
            for codon in codons[rna[i:i+2]]:
                if codon == rna[i+2]:
                    protein += codons[rna[i:i+2]][rna[i+2]]
        i += 3
    return protein


# testing
print(rna_to_protein('AUGUAUUGCGCCAAGGAGUAG'))
# Output: MYCAKE

