"""
Created on Mon Dec 08 20:05:16 2014

@author: choog_000
"""
list = []

limit = range(1000)

for x in limit:
    if x%3 == 0:
        list.append(x)
    elif x%5 == 0:
        list.append(x)

daSum = sum(list)
print daSum