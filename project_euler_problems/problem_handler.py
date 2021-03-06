#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from importlib import import_module


def get_solution(number):
    """
    Imports the project euler solutions in python and retrieves the
    solution function on demand.
    """
    problem_name = "problem_" + str(number)
    name = ".solved_problems.python_solutions." + problem_name
    imp = import_module(name, package="project_euler_problems")
    solution_ptr = getattr(imp, problem_name)
    return solution_ptr


class Problem:
    """
    A project euler problem is its index number, name, and description.
    This class allows us to initialize a problem, show its info, and solve it.
    """

    def __init__(self, prob_number, prob_name, prob_desc, prob_solution):
        """
        Required problem number, name, description, and solution function.
        """
        self.number = prob_number
        self.name = prob_name
        self.desc = prob_desc
        self.solution = prob_solution

    def show_info(self):
        """
        Display available information on the problem.
        """
        print("Problem number: " + str(self.number))
        print("Problem name: " + str(self.name))
        print("Problem description: " + str(self.desc))

    def solve(self):
        """
        Solve the project euler problem and print the answer.
        """
        print("Problem %s Answer: %s" % (self.number, self.solution()))


# Create a list that contains the object for each solved problem.
all_problems = []

# Create the Problem object for each solved problem.
P1 = Problem(
    1,
    "Multiples of 3 and 5",
    "Sum up all the multiples of 3 and 5 below 1000",
    get_solution(1),
)
P2 = Problem(
    2,
    "Even Fibonacci numbers",
    "Sum of even-valued Fibonacci numbers under 4M.",
    get_solution(2),
)
P3 = Problem(
    3,
    "Largest Prime Factor",
    "Find the largest prime factor of 600851475143.",
    get_solution(3),
)
P4 = Problem(
    4,
    "Largest Palindrome Product",
    "Find the largest palindrome made from the " + "product of two 3-digit numbers.",
    get_solution(4),
)
P5 = Problem(
    5,
    "Smallest Multiple",
    "Find the smallest positive number that is evenly divisible "
    + "by all of the numbers from 1 to 20?",
    get_solution(5),
)
# Add all Problem instances into the list of all_problems (solved).
all_problems.extend([P1, P2, P3, P4, P5])
