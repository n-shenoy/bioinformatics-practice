#!/usr/bin/env python
#/mnt/c/Users/navam/OneDrive/Documents/GitHub/bioinformatics-practice

""" Finding the reverse complement of a DNA strand """

__author__ = "Navami Shenoy"

import kmer_index

def reverse_complement(string):
    reversed_string = string[::-1]  # reverse the string
    rev_comp_string = ''
    
    base_complement = {'A':'T', 'T':'A', 
                        'G':'C', 'C':'G'}
    # find the complement of the reversed string
    for base in reversed_string:
        rev_comp_string = rev_comp_string + base_complement[base]

    return rev_comp_string 


def recursive(matrix,i=0,j=0, length=0,palindromes = []):
   if i != len(matrix) and j != len(matrix): 
    if matrix[i][j] == 0:
        palindromes.append((i,length+1, matrix[i][j]))
        if matrix[i+1][j+1] == 0:
            recursive(matrix, i+1,j+1,length+1,palindromes)
        else:
            recursive(matrix, i,j+1,length,palindromes)
    return palindromes 
    


def reverse_palindrome(string, min_length, max_length):
    rev_comp_string = reverse_complement(string) 
    matrix = []
    
    for i in range(len(string)):
        matrix.append([0]*(len(rev_comp_string)))     

    for i in range(len(string)): # first column
        for j in range(len(rev_comp_string)):
            if string[i] == rev_comp_string[j]:
                matrix[j][i] = 1
            else:
                matrix[j][i] = 0
    palindromes = recursive(matrix)   

    diagonal_sums = []
    #diagonal_sums.append(matrix[-1][0])

    sum = 0
    for i in range(len(rev_comp_string)-1):
        for j in range(len(string)-1):
        sum = matrix[i][j] + matrix[i+1][j+1]

    
    return rev_comp_string, matrix, palindromes

def editDistance(x,y): # two strings, X and Y
    # we create a matrix we'll fill in with the edit distances 
    # for the substrings that we already computed to save time,
    
    D = [] # matrix D initialized as X+1 by Y+1 array of zeroes
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))   
    
    # any prefix of length x and an empty prefix y will have an 
    # edit distance of x. So we initialize the first row and first 
    # column with the values of x and y:
    for i in range(len(x)+1): # first column
        D[i][0] = i  
    for i in range(len(y)+1): # first row
        D[0][i] = i
        
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            # move horizontally from the cell to the left:
            distHor = D[i][j-1] + 1
            # vertical distance from the cell above it:
            distVer = D[i-1][j] + 1
            # is these 2 characters match, then the edit distance
            # for the diagonal cell will not increase:
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else: # if they don't match, add 1
                distDiag= D[i-1][j-1] + 1
            
            # now we have 3 possible edit distances for this cell
            # so we pick the minimum of the three values:
            D[i][j] = min(distHor, distVer, distDiag)
        
    # after the matrix has been populated, we want the 
    # edit distance in the cell for the last row and the last column
    # this edit distance is the edit distance between the entire 
    # two strings X and Y
    return D, D[-1][-1]



 
                

# testing
st = 'TCAATGCATGCGGGTCTATATGCAT'
#print(reverse_palindrome(st,4,12))

test = 'AGCATGCAT'
print(reverse_palindrome(test,4,12))
# Output: ATGCATATAGACCCGCATGCATTGA 

test_r = reverse_complement(test)
print(editDistance(test,test_r))
print('global alignment: ')
print(global_alignment(test,test_r))




