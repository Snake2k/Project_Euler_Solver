#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def problem_1():
    answer = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            answer += x
    return answer

if __name__ == "__main__":
    print("Problem 1 Answer: " + str(problem_1()))
