#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #20:

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

sums = 1

for x in range(100, 0, -1):
    sums *= x

sums = [int(i) for i in str(sums)]
print "Sum of digits in 10!:", sum(sums)  # Answer: 648
