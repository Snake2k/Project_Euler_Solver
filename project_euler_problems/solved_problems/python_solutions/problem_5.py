#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def problem_5():
    """
    List shortened by hand because if any number is divisible 
    by 20 then it is evenly divisible by 2, 4, 5, 10. 
    Same goes for 18.
    Kept 11, 13, 17, 19 because they are prime numbers.
    Kept 14 because of 7.
    Kept 16 because of 8.
    Kept 18 because of 9.
    Removed 1 because all ints are divisible by 1.
    Starting and stepping with 2520 because it is divisible 
    by all in list.
    Any number divisible by 2520 is divisible by the rest.
    """
    number = 2520
    divisors = [11, 13, 14, 16, 17, 18, 19, 20]
    while True:
        for x in divisors:
            if number % x == 0:
                ans = number
                found = True
            else:
                ans = None
                found = False
                break
        if found:
            break
        else:
            number += 2520
    return number


if __name__ == "__main__":
    print("Problem 5 Answer: " + str(problem_5()))
