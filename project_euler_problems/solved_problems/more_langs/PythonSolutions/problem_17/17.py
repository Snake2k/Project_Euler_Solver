#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #17:

If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

NumbersTo9  = [ 'one',
                'two',
				'three',
				'four',
				'five',
				'six',
				'seven',
				'eight',
				'nine' ]

Tens2to9 = [ 'twenty',
			 'thirty',
			 'forty',
			 'fifty',
			 'sixty',
			 'seventy',
			 'eighty',
			 'ninety' ]

Unique = [ 'ten',
		   'eleven',
		   'twelve',
		   'thirteen',
		   'fourteen',
		   'fifteen',
		   'sixteen',
		   'seventeen',
		   'eighteen',
		   'nineteen' ]

Alphabets = 0

# 1 - 9
for num in NumbersTo9:
	Alphabets += len(num)

# 10 - 19
for num in Unique:
	Alphabets += len(num)

# 20 - 99
for ten in Tens2to9:
	Alphabets += len(ten)
	for num in NumbersTo9:
		Alphabets += len(ten) + len(num)

# 100 - 109 then 200 - 209 then 300 - 309 etc
for num in NumbersTo9:
	Alphabets += len(num) + len("hundred")
	for numagain in NumbersTo9:
		Alphabets += len(num) + len("hundred") + len("and") + len(numagain)

# 110 - 119 then 210-219 then 310-319 etc
for num in NumbersTo9:
	for uninum in Unique:
		Alphabets += len(num) + len("hundred") + len("and") + len(uninum)

# 120-190 then 220-290 then 320-390 etc
for num in NumbersTo9:
	for ten in Tens2to9:
		Alphabets += len(num) + len("hundred") + len("and") + len(ten)

# 121-129 then 131-139.. 221-229.. 920-929 etc
for num in NumbersTo9:
	for ten in Tens2to9:
		for renum in NumbersTo9:
			Alphabets += len(num) + len("hundred") + len("and") + len(ten) + len(renum)

Alphabets += len("one") + len("thousand")
print "Letters used:", Alphabets # Answer: 21124
