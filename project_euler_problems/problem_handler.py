#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import problems that have been solved.
from solved_problems.python_solutions.problem_1 import problem_1
from solved_problems.python_solutions.problem_2 import problem_2
from solved_problems.python_solutions.problem_3 import problem_3

# A problem itself is pretty much its index number, name, description.
# This object lets us tie that information to a solution function.
class Problem():
    def __init__(self, prob_number, prob_name, prob_desc, prob_solution):
        self.number = prob_number
        self.name = prob_name
        self.desc = prob_desc
        self.solution = prob_solution
    def show_info(self):
        print("Problem number: " + str(self.number))
        print("Problem name: " + str(self.name))
        print("Problem description: " + str(self.desc))
    def solve(self):
        print("Problem %s Answer: %s" % (self.number, self.solution()))

# Create a list that contains the object for each solved problem.
all_problems = []
P1 = Problem(
        1,
        "Multiples of 3 and 5",
        "Sum up all the multiples of 3 and 5 below 1000",
        problem_1
)
P2 = Problem(
        2,
        "Even Fibonacci numbers",
        "Sum of even-valued Fibonacci numbers under 4M.",
        problem_2
)
P3 = Problem(
        3,
        "Largest Prime Factor",
        "Find the largest prime factor of 600851475143.",
        problem_3
)
all_problems.append(P1)
all_problems.append(P2)
all_problems.append(P3)
