#!/usr/bin/env python

""" Locating Restriction Sites: Finding all reverse palindromes
    occuring in a genetic sequence """

__author__ = "Navami Shenoy"


# helper function
def reverse_complement(string):
    # returns the reversed complement of a string
    reversed_string = string[::-1]  # reverse the string
    rev_comp_string = ''
    
    base_complement = {'A':'T', 'T':'A', 
                        'G':'C', 'C':'G'}
    # find the complement of the reversed string
    for base in reversed_string:
        rev_comp_string = rev_comp_string + base_complement[base]

    return rev_comp_string 


def reverse_palindrome(string, min_length, max_length):
    """ return the positions and lengths of all reverse palindromes
        occuring in a string """
    palindromes = []  # [(position, length of the reverse palindrome)]

    # compare each possible substring of the string 
    # with that of the complement in reverse:
    for i in range(len(string)):
        # look for substrings of lengths within a given range:
        for j in range(min_length,max_length+2):
            # compare each substring (or k-mer of length in given range)
            # with the reverse complement of that substring
            if string[i:i+j] == reverse_complement(string[i:i+j]) and len(string) >= (i+j):
                    palindromes.append((i+1,j))
            
    return palindromes # return all unique reverse palindromes

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

