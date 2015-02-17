# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 21:29:50 2014

@author: choog_000
"""
##Project Euler: Problem 2 - Even Fibonacci Numbers

fibList = [1,2]
values = range(35)
fourMil = 4000000

#reproduces the Fibonacci sequence up to a value which does not exceed 
#four million

for item in values:
    if fibList[-1] < fourMil:    
        fibList.append((fibList[-2] + fibList[-1]))
    else:
        print "The sequence's value has now exceeded four million."

#to test the sequence's length and to set an appropriate "values" element
print len(fibList)
#turns out fibList is around 33

#the last term, which summed the final two terms in the fibList, should now 
#exceed fourMil. Below chops off the last number to ensure we stay below the limit.

if fibList[-1] > fourMil:
    del fibList[-1]    
else:
    print "The final value in the sequence did not exceed four million."
    
print fibList

#initiates a list of even-valued terms  
evenTerms = [0]

#iterates over all values in the Fibonacci sequence to determine which values
#to include in the evenTerms list
for item in fibList:
    if item%2 == 0:
        evenTerms.append(item)
    else:
        print "Odd number"

print evenTerms
        
#Sums the elements from our new evenTerms list, providing us with our answer       
daSum = sum(evenTerms)
print "Your final answer is " + str(daSum)
