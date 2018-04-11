#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #16:

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

toPower = 2**1000
Sum = 0
for digit in str(toPower):
	Sum += int(digit)

print "Sum:", Sum # Answer: 1366
