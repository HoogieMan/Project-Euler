import math
##Project Euler -- Problem 3
#What is the largest prime factor of 600851475143?

# test function to execute --> PrimeFactorMetaFxn(13195)
# function to execute --> PrimeFactorMetaFxn(600851475143)

#meta function to bring it all together
def PrimeFactorMetaFxn(daNum):
    answer = max_prime_factor(is_prime(list_all_factors(daNum)))
    print "The answer is " + str(answer)    
    return answer         
  
#create a list of all possible factors
def list_all_factors(daNum):
    factorList = []
    daNumRoot = math.sqrt(daNum)
    possFactor = xrange(1,int(daNumRoot))
    #loop through range up to daNum, id those which are factors
    for x in possFactor:
        if daNum%x == 0:
            factorList.append(x)
    
    return factorList

#determine which items in list are prime
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
   
#return the highest prime factor
def max_prime_factor(primeFactors):
    maximumPrime = max(primeFactors)
    #print "maximumPrime is " + str(maximumPrime)
    return maximumPrime
    