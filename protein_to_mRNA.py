#!/usr/bin/env python

""" Inferring mRNA from Protein: Calculating how many mRNA
    sequences code for a single amino acid sequence """

__author__ = "Navami Shenoy"

codon_table = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}
 
amino_acids = {} # {'amino acid': frequency}
# count how many codons code for 
# the same amino acid 
for acid in codon_table.values():
    if acid not in amino_acids:
        amino_acids[acid] = 1
    else:
        amino_acids[acid] += 1

#print(amino_acids)

def protein_to_mRNA(protein):
    """ return the number of possible mRNA sequences
        that code for the given protein sequence """ 

    num_mrna = amino_acids['Stop'] #stop codons
    for acid in protein: 
        num_mrna = (num_mrna*amino_acids[acid]) % 1000000 #storing large numbers
    return num_mrna


# testing
test_file = open('rosalind_mrna.txt') # source: https://rosalind.info
protein = test_file.read().rstrip()
test_file.close()
print(protein_to_mRNA(protein)) 
#Output: 311936