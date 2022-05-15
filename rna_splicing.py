#!/usr/bin/env python

""" Splicing RNA: removing exons from a DNA sequence and transcribing 
    and translating it into a amino acid sequence """

__author__ = "Navami Shenoy"

import dna_to_rna as dna
import rna_to_protein as rna


def splicing(dna_string, introns):
    """ returns the amino acid sequence after splicing introns,
        transcribing DNA, and translating RNA into protein""" 

    # splicing
    for intron in introns: # for every intron in the list
        if intron in dna_string: # if intron exists in the string
            dna_string = dna_string.replace(intron,'') # remove intron
    spliced_string = "".join(dna_string) # concatenate exons

    #transcription
    spliced_rna = dna.dna_to_rna(spliced_string) 
    #translation
    protein = rna.rna_to_protein(spliced_rna) 
    return protein


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
seqs = readFASTA('rosalind_splc.txt') # test file source: https://rosalind.info
seqs = list(seqs.values())
dna_string = seqs[0] # the DNA string
introns = seqs[1:] # the list of introns
print(splicing(dna_string, introns)) 
# Output: MAGRSRDMGSRPAAQVFCFAVRYPWGSPGSSFQYCNASRARSDCTSHFSSSLCQTCRVRALPSSMTLHDRLVHGCGGRRLPDTAILKTFQRNRMRTNLRHRATDVRSNLYSSAPFGSPKVLHPFSKRLFRSTMGFSPAAYSPKPRTRSCALFSKGVRVSRMLSRLRQPSARPPCSEVSHTPRTFVRGSSRRQRATLNG

