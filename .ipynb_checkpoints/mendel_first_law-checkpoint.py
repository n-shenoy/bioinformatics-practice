#!/usr/bin/env python

""" Finding the probability of an offspring exhibiting the dominant
    phenotype resulting from randomly selected mating organisms from
    a population (assuming that any two organisms can mate) """

__author__ = "Navami Shenoy"

# Updated with a better implementation:
    # the new algorithm helps us find any kind of probability 
    # from the population 
    
def punnett_square(p1, p2):
    """ creates a punnett square for the genotypes of
        any two given parents, p1 and p2. Returns an array
        containing the number of dominant and recessive offsprings
        resulting from the cross """ 
    all_progeny = np.array([['  ' , '  '], 
                            ['  ', '  ']])
    dominant = 0
    recessive = 0
    for i in range(0,2):
        for j in range(0,2):
            offspring = sorted(p1[i] + p2[j])
            all_progeny[j][i] = ''.join(offspring)
            if all_progeny[j][i].islower(): # if recessive genotype
                recessive += 1
            else:
                dominant += 1
    
    return dominant, recessive

# test:
# punnett_square('Tt','Tt')
# Output: (3, 1)  

def dominant(k,m,n):
    """ returns the probability of getting an offspring with
        a dominant phenotype if two randomly selected individuals
        from a population are mated """ 
    # in this population,
        # k individuals are homozygous dominant
        # m individuals are heterozygous dominant
        # n individuals are homozygous recessive
    prob = []
    population = [k, m, n]
    total = k+m+n
    genotypes = ['TT', 'Tt', 'tt']
    for i in range(len(genotypes)):
        for j in range(len(genotypes)):
            dominant, recessive = punnett_square(genotypes[i], 
                                                 genotypes[j])
            if dominant != 0:  # filters out cases where no offspring can have dominant phenotype
                parent1 = population[i]
                if genotypes[i] == genotypes[j]: # both parents have the same genotype
                    parent2 = population[j] - 1  
                else: # parents have different genotypes
                    parent2 = population[j]
                num = (dominant*parent1*parent2) / (4*total*(total-1))
                prob.append(num)
                
    return sum(prob)


# testing
# population consisting of 55 individuals,
# 19 homozygous dominant,
# 18 heterzygous dominant
# 18 homozygous recessive
dominant(19,18,18)
# Output: 0.7621212


""" Older implementation """
#def probability_dominant(k,m,n):
#    """ Assuming that any two organisms can mate,
#       find the probability that, if two randomly selected
#        ndividuals from a population mate, the offspring 
#        produced has a dominant allele and therefore has a 
#        dominant phenotype. """
#    total = k+m+n  # total population
#    prob = []

    # probability of getting...
#    prob.append((k/total)*((k-1)/(total-1))) # k and k
    
#    """ only 75% of offsprings produced from two heterozygous
#        dominant individuals will have a dominant phenotype """
#    prob.append((m/total)*((m-1)/(total-1))*0.75) # m and m
   
#    prob.append((k/total)*((m)/(total-1))) # k and m
#    prob.append((m/total)*((k)/(total-1))) # m and k
    
#    prob.append((k/total)*((n)/(total-1))) # k and n
#    prob.append((n/total)*((k)/(total-1))) # n and k
    
#    """ only 50% of offsprings produced from a heterozygous
#        dominant and a homozygous recessive parent
#        will have a dominant phenotype """
#    prob.append((m/total)*((n)/(total-1))*0.5) # m and n
#    prob.append((n/total)*((m)/(total-1))*0.5) # n and m
    
#    return sum(prob)