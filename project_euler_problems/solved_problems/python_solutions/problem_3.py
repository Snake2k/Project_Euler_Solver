#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def problem_3():
    number = 600851475143
    x = 2
    answer = 1
    while number > 1:
        if number % x == 0:
            answer = x
            number = number / x
            while number % x == 0:
                number = number / x
        x += 1
    return answer

if __name__=="__main__":
    print("Problem 3 Answer: " + str(problem_3()))
