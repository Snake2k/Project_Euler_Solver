#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20?
"""

"""
List shortened by hand because if any number is divisible by 20 it is evenly
divisible by 2, 4, 5, 10. Same goes for 18. 11, 13, 16, 19 are prime
kept 14 because of 7 and 16 because of 8. Took away 9.
Starting and stepping with 2520 because it is divisible by all in list.
Any number divisible by 2520 is divisible by the rest.
And 1 because all ints are divisible by 1.
"""
import time
number = 2520
divisors = [11, 13, 14, 16, 17, 18, 19, 20]
start = time.time()
while True:
	for x in divisors:
		if number % x == 0:
			ans = number
			found = True
		else:
			ans = None
			found = False
			break
	if found:
		break
	else:
		number += 2520
print "Answer:", number #Answer: 232792560
