#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #15:

Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

Image: http://projecteuler.net/problem=15

How many such routes are there through a 20×20 grid?
"""

def factorial(n):
	total = 1
	for x in range(n, 0, -1):
		total *= x
	return total

width, height = 20, 20

routes = factorial(width + height)/(factorial(width) * factorial(height))

print "Number of routes in 20x20 grid:", Routes # Answer: 137846528820
