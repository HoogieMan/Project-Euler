# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:20:27 2015

@author: choog_000
"""
##Project Euler -- Problem 3
def PrimeFactorMetaFxn(daNum):
    answer = max_prime_factor(is_prime(list_all_factors(daNum)))
    #is_prime(factorList)
    #return max_prime_factor(primeFactors)
    print "The answer is " + str(answer)    
    return answer         
##the below functions work and correctly
##generate the test answer (29 for test 13195)
##however, receiving an overflow error 'range()
##result has too many items'
  
#def daPrimeFactorMetaFxn(daNum, factorList, primeFactors):
#    list_all_factors(daNum)
#    is_prime(factorList)
#    answer = max_prime_factor(primeFactors)
#    print "The answer is " + str(answer)
#  
def list_all_factors(daNum):
    factorList = []
    possFactor = xrange(1,daNum)
    
    #loop through range up to daNum, id those which are factors
    for x in possFactor:
        if daNum%x == 0:
            factorList.append(x)
    
    #print "factorList is " + str(factorList)
    return factorList

def is_prime(factorList):
    primeFactors = []    
    for factor in factorList:
        newFactorList = []    
        for x in xrange(1,factor):
            if factor%x == 0:
                newFactorList.append(x)
                #print "newFactorList is " + str(newFactorList)
            #else:
                #print str(factor) + " does not divide evenly by " + str(x)
        if len(newFactorList) == 1:
            primeFactors.append(factor)    
    print "primeFactors are " + str(primeFactors)
    return primeFactors 
    
def max_prime_factor(primeFactors):
    maximumPrime = max(primeFactors)
    #print "maximumPrime is " + str(maximumPrime)
    return maximumPrime
    