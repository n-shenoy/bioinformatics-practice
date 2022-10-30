#!/usr/bin/env python

""" Finding the molecular mass of a protein"""

__author__ = "Navami Shenoy"

import requests
from bs4 import BeautifulSoup
import pandas as pd

#get monoisotopic masses of amino acid residues
url = 'https://en.wikipedia.org/wiki/Proteinogenic_amino_acid#Mass_spectrometry'
tables = pd.read_html(url)
df = tables[3]
aa = list(df['Short']) #amino acid residues
masses = list(df['Mon. mass§ (Da)']) #monoisotopic masses
aa_mass = {aa[i]: masses[i] for i in range(len(aa))}
  

def protein_mass(string):
    #calculate sum of monoisotopic masses of
    #each amino acid residue in the protein
    mass = 0.0
    for letter in string:
        mass = mass + float(aa_mass[letter])
    return round(mass, 3)


# testing 
print(protein_mass('SKADYEK'))
# Output: 821.392   
with open('rosalind_prtm.txt') as f: # Test file source: www.rosalind.info 
    sequence = f.read().rstrip()
    print(protein_mass(sequence))  
# Output: 102092.494