#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Project Euler Problem #27:

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values 
n = 0 to 39. 
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values n = 0 to 79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number of primes 
for consecutive values of n, starting with n = 0.
"""
import time

def formula(n, a, b):
    value = n**2 + a * n + b
    value = abs(value)
    return value

def isPrime(n):
    if n == 2:
	return True
    elif n < 2:
	return None
    for x in range(2, n):
	if n % x == 0:
            return False
    return True

mostPrimes = 0
Product = 0
starttime = time.clock()
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
	primes = 0
	n = 0
	while isPrime(formula(n, a, b)):
            n += 1
	    primes += 1
	    if primes > mostPrimes:
		mostPrimes = primes
		Product = a*b

print "\nThe product of a and b having max primes:", Product # Answer: -59231
print "Time to finish program: %s seconds\n" % (time.clock() - starttime)
