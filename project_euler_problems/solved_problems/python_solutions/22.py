#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #22:

Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list 
to obtain a name score.

For example, 
when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import string

namesFile = open("./problem_22_names.txt", "r")
lines = namesFile.read()
lines = lines.split(",")
lines = sorted(lines)

Letters = string.lowercase

Alphabets = {}
for x in range(1, len(Letters) + 1):
    Alphabets[Letters[x - 1]] = x

Sum = 0
for word in lines:
    wordSum = 0
    for letter in word.lower():
        if letter != '"':
            wordSum += Alphabets[letter]
    Sum += wordSum * (lines.index(word) + 1)

print "Total of all name scores:", Sum  # Answer: 871198282
