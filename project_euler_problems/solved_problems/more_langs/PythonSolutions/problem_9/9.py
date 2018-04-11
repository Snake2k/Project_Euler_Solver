#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for A in xrange(1, 1001):
	for B in xrange(A+1, 1001):
		for C in xrange(B+1, 1001):
			if A*A + B*B == C*C and A+B+C == 1000:
				print "A: %d\nB: %d\nC: %d" % (A, B, C)
				print "Sum: %d\nProduct: %d" % (A+B+C, A*B*C) #Answer: 31875000
				break
