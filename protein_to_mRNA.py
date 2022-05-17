#!/usr/bin/env python

""" Inferring mRNA from Protein: Calculating how many mRNA
    sequences code for a single amino acid sequence """

__author__ = "Navami Shenoy"


def protein_to_mRNA(protein):
    # table
    amino_acids = { 'A': , 
                    'R': ,
                    'N': ,
                    'D': ,
                    'C': ,
                    'Q': ,
                    'E': ,
                    'G': ,
                    'H': ,
                    'I': ,
                    'L': ,
                    'K': , 
                    'M': , 
                    'F': ,
                    'P': ,
                    'S': ,
                    'T': ,
                    'W': ,
                    'Y': ,
                    'V': 
                }


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


# testing
