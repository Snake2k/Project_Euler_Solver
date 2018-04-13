#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def problem_4():
    answer = 0
    for x in range(99, 1000):
        for y in range(99, 1000):
            product = x * y
            if str(product) == str(product)[::-1] and \
               product > answer:
                answer = product
    return answer

if __name__ == "__main__":
    print("Problem 4 Answer: " + str(problem_4()))
