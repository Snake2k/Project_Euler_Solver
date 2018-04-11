#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def getMultiples(below, *args):
    multiples = []
    for number in args:
        for x in range(1, below):
            if x%number==0:
                multiples.append(x)
            else:
                pass
    return multiples

#Get multiples below 1000 of 3 and 5
#Set list in order to remove duplication of multiples i.e; 15
listOfMultiples = getMultiples(1000, 3, 5)
listOfMultiples = set(listOfMultiples)
print sum(listOfMultiples) #Answer = 233168
