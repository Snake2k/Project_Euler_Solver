#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def isPrime(number):
	Prime = None
	if number == 2:
		return True
	elif number < 2:
		raise ValueError("Incorrect number.")
	else:
		divisor = 2
		for x in range(divisor, number):
			if number % x == 0:
				return False
			else:
				Prime = True
	return Prime

Primes = []
x = 2
while len(Primes) < 10001:
	if isPrime(x):
		Primes.append(x)
	x += 1

print "10,001st Prime:", max(Primes) #Answer: 104743
