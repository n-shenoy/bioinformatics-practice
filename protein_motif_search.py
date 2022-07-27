#!/usr/bin/env python

""" Finding all occurrences of N-glycosylation motif in a protein"""

__author__ = "Navami Shenoy"

import requests
import bisect as bi

def fetchFASTA(protein_id):
    url = 'https://www.uniprot.org/uniprot/'
    data = requests.get(url+protein_id+".fasta")
    sequence = data.text.split('\n')
    return "".join(sequence[1:])

def n_gly_motif_search(protein_id):
    sequence = fetchFASTA(protein_id)
    positions = []

    for i in range(0, len(sequence)-3):
        if sequence[i] == 'N' and sequence[i+1] != 'P' and sequence[i+3] != 'P':
            if sequence[i+2] == 'S' or sequence[i+2] == 'T':
                positions.append(i+1)
    
    return protein_id, positions
    

# testing 
protein_id, positions = n_gly_motif_search('B5ZC00')
print(protein_id)
print(*positions)
# Output: B5ZC00     
#         85 118 142 306 395     

# testing
with open('rosalind_mprt.txt') as f:
    protein_IDs = f.read().split("\n")
    for ID in protein_IDs:
        protein_id, positions = n_gly_motif_search(ID)
        if len(positions) != 0:
            print(protein_id)
            print(*positions)
        
