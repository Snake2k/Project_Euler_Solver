#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #25:

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

X = 1
Y = 1

Sum = X + Y
Fib = 3 # X = Fib 1, Y = Fib 2, Sum = Fib 3.....N till it ends

while len(str(Sum)) < 1000:
	X = Y
	Y = Sum
	Sum = X + Y
	Fib += 1

print "First term to contain 1000 digits: Fib #" + str(Fib) # Answer: 4782
