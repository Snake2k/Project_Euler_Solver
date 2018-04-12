#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #24:

A permutation is an ordered arrangement of objects. 
For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. 

The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

Numbers = [str(x) for x in range(0, 10)]
N = len(Numbers)
count = 0
limit = 1000000 - 1

while count < limit:
	X = N - 2
	Y = N - 1
	while not Numbers[X] < Numbers[X+1]:
		X -= 1
	while not Numbers[Y] > Numbers[X]:
		Y -= 1
	Numbers[X], Numbers[Y] = Numbers[Y], Numbers[X]
	Numbers[X+1:] = reversed(Numbers[X+1:])
	count += 1

Answer = ""
for Num in Numbers:
	Answer += Num

print "Millionth Lexicographic Permutation:", Answer # Answer: 2783915460
