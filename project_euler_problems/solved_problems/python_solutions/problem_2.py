#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def problem_2():
    answer = 0
    first = 0
    second = 1
    third = first + second
    while third < 4000000:
        first = second
        second = third
        third = first + second
        if third % 2 == 0:
            answer += third
    return answer

if __name__=="__main__":
    print("Problem 2 Answer: " + str(problem_2()))

