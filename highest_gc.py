#!/usr/bin/env python

""" Finding the sequence with the highest GC content """

__author__ = "Navami Shenoy"


def highest_gc(file):
    # calculates the GC content of multiple sequences in a file
    # returns the ID of the string containing the highest GC content,
    # followed by its GC content
    gc_content = {}
    seq = ' '
    with open(file, 'r') as f:
        # create a dictionary of IDs and sequences
        for line in f: 
            if line[0] == '>' and seq != '':
                label = line[1:].rstrip()
                seq = ''
            else:
                seq += line.rstrip()
                gc_content[label] = seq
             
        # calculate GC content of each sequence in the dictionary
        for label in gc_content: 
            seq = gc_content[label] 
            gc_content[label] = ((seq.count('G')+seq.count('C'))/len(seq))*100
        
        # find the sequence with the highest GC content and its ID
        highest_gc =  max(gc_content.values())
        gc_id = next((label for label, gc in gc_content.items() 
                      if gc == highest_gc), None)
    f.close()
    return (gc_id, highest_gc)



# testing
# test file: 'rosalind_gc.txt', source: https://rosalind.info/
print(highest_gc(file)[0]) # get sequence ID
print(highest_gc(file)[1]) # get highest GC content
# Output: Rosalind_9126, 51.86972255729795