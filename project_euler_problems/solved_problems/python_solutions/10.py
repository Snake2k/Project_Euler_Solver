#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# Algorithm: Sieve of Eratosthenes:
# Deletes the multiples of all primes upto a given number.
import time

start = time.time()
Sieve = [True] * 2000000

def mark(Sieve, X):
    for i in xrange(X * 2, len(Sieve), X): # Loops for all multiples.
        Sieve[i] = False # Deletes the possibility.

for x in xrange(2, len(Sieve)):
    if Sieve[x]:
        mark(Sieve, x)

print "Sum of all primes < 2m:", sum([i for i in xrange(2, len(Sieve)) if Sieve[i]]) #Answer: 142913828922
print "Time to finish: ", str(time.time() - start), "seconds."
