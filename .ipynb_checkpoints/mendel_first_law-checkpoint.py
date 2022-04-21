#!/usr/bin/env python

""" Finding the probability of an offspring exhibiting the dominant
    phenotype resulting from randomly selected mating organisms from
    a population """

__author__ = "Navami Shenoy"


def probability_dominant(k,m,n):
    """ Assuming that any two organisms can mate,
        find the probability that, if two randomly selected
        individuals from a population mate, the offspring 
        produced has a dominant allele and therefore has a 
        dominant phenotype. """
    # in this population,
    # k individuals are homozygous dominant
    # m individuals are heterozygous dominant
    # n individuals are homozygous recessive
    total = k+m+n  # total population
    prob = []
    
    # probability of getting...
    prob.append((k/total)*((k-1)/(total-1))) # k and k
    
    """ only 75% of offsprings produced from two heterozygous
        dominant individuals will have a dominant phenotype """
    prob.append((m/total)*((m-1)/(total-1))*0.75) # m and m
   
    prob.append((k/total)*((m)/(total-1))) # k and m
    prob.append((m/total)*((k)/(total-1))) # m and k
    
    prob.append((k/total)*((n)/(total-1))) # k and n
    prob.append((n/total)*((k)/(total-1))) # n and k
    
    """ only 50% of offsprings produced from a heterozygous
        dominant and a homozygous recessive parent
        will have a dominant phenotype """
    prob.append((m/total)*((n)/(total-1))*0.5) # m and n
    prob.append((n/total)*((m)/(total-1))*0.5) # n and m
    
    return sum(prob)



# testing
# population consisting of 55 individuals,
# 19 homozygous dominant,
# 18 heterzygous dominant
# 18 homozygous recessive
probability_dominant(19,18,18)
# Output: 0.7621212

