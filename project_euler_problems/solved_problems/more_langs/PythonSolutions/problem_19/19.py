#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #19:

You are given the following information, 
but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, 
	but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
"""

Months = {'Jan' : 31,
		  'Feb' : 0,
		  'Mar' : 31, 
		  'Apr' : 30, 
		  'May' : 31, 
		  'June' : 30, 
		  'July' : 31, 
		  'Aug' : 31, 
		  'Sep' : 30, 
		  'Oct' : 31, 
		  'Nov' : 30, 
		  'Dec' : 31 }
Days = ['monday', 
        'tuesday', 
		'wednesday', 
		'thursday', 
		'friday', 
		'saturday', 
		'sunday']
Years = [i for i in range(1900, 2001)]
Week = 7

sundaycount = 0

Daycount = 0

CurDate = None
for yr in Years:
	if yr % 400 == 0:
		Months['Feb'] = 29
	else:
		Months['Feb'] = 28
	for m in Months:
		for d in range(1, Months[m] + 1):
			CurDate = str(Days[Daycount]), str(d) + 'st', str(m), str(yr)
			Daycount += 1
			if Daycount % 7 == 0:
				Daycount = 0
			if Days[Daycount] == 'sunday' and d == 1:
				sundaycount += 1

print "Sundays:", sundaycount # Answer: 171
