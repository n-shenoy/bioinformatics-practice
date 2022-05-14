#!/usr/bin/env python

""" Locating Restriction Sites: Finding all reverse palindromes
    occuring in a genetic sequence """

__author__ = "Navami Shenoy"


def reverse_palindrome(string, min_length, max_length):
    """ return the positions and lengths of all reverse palindromes
        occuring in a string """
    palindromes = []  # [(position, length of the reverse palindrome)]

    # find the complement of the DNA string
    complement = ''
    base_complement = {'A':'T', 'T':'A', 
                        'G':'C', 'C':'G'}
    for base in string:
        complement = complement + base_complement[base]

    # compare each possible substring of the string 
    # with that of the complement in reverse:
    for i in range(len(string)-min_length):
        # look for substrings of lengths within a given range:
        for j in range(min_length,max_length+1):
            # traverse both strings in the forward direction, but
            # compare each substring of the original string with the
            # reverse of the corresponding substring of the complement
            if string[i:i+j] == complement[i:i+j][::-1]:
                if len(string) >= (i+j):
                    palindromes.append((i+1,j))
                else:
                    palindromes.append((i+1,len(string)-i))
    return set(palindromes) # return all unique reverse palindromes

# testing
string = 'TCAATGCATGCGGGTCTATATGCAT'
palindromes = reverse_palindrome(string, min_length = 4, max_length = 12)
for position, length in palindromes: print(position, length)
# Output: 
# 4 6
# 5 4
# 6 6
# 7 4
# 17 4
# 18 4
# 20 6
# 21 4

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:    # f is the name for the filename variable
        for line in f:
            if line[0] != '>':
                genome += line.rstrip() # rstrip removes spaces, tabs, \n
    return genome
 
#filename = open('rosalind_revp.txt')

dna = readGenome('rosalind_revp.txt')

palindromes = reverse_palindrome(dna, min_length = 4, max_length = 12)
#for position, length in palindromes: print(position, length)