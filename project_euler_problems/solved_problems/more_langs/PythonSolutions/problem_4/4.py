#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #4:

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalin(x):
	if type(x) == int:
		x = str(x)
	if x == x[::-1]:
		return True
	else:
		return False

palin = 0
for x in range(99, 1000):
	for y in range(99, 1000):
		product = x * y
		if isPalin(product) and product > palin:
			palin = product

print "Largest Palindrome:", palin #Answer: 906609
