#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #12:

The sequence of triangle numbers is generated by adding 
the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
We can see that 28 is the 1st triangle number to have over five divisors.
What is the value of the 1st triangle number to have over 500 divisors?
"""

import time

start = time.time()
limit = 1
number = 0
divs = []
while True:
    for y in range(1, limit + 1):
        number += y
    for x in range(1, int(number ** 0.5) + 1):
        if number % x == 0:
            divs.append(x)
    if len(divs) * 2 > 500:
        break
    else:
        limit += 1
        divs = []
        number = 0

print "1st Triangle Number with 500 divs:", number  # Answer: 76576500
print "Time taken: ", str(time.time() - start)
