# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 21:29:50 2014

@author: choog_000
"""

startList = [1,2]
values = [1]

#reproduces the Fibonacci sequence up to a value which does not exceed the one
#set in the first line below

if startList[-1] < 500:    
    for item in values:
        startList.append((startList[-2] + startList[-1]))
else:
    print "The sequence's value has exceeded four million."
  
#initiates a list of even-valued terms  
evenTerms = [0]

#iterates over all values in the Fibonacci sequence to determine which values
#to include in the evenTerms list
for item in startList:
    if item%2 == 0:
        evenTerms.append(item)
    else:
 
#Sums all even-valued terms from our new list, providing us with our answer       
daSum = 

startList[0] + startList[1]
print newList

startList[0] + startList[1]
