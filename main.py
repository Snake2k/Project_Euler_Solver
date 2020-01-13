#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This program lists all of the solved project euler problems and then
# asks the user which one they would like to solve.
# It also prints a short description of the problem before running.
import os
from sys import exit
from time import sleep
from project_euler_problems.problem_handler import all_problems


def clear_screen():
    """
    This cleans any previous output on the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def problem_lookup(lookup_number, problem_list):
    """
    Takes a problem number and a list of problems and returns the problem.
    """
    for problem in problem_list:
        if problem.number == lookup_number:
            return problem
    return None


if __name__ == "__main__":
    # Run till the user explicitly chooses to exit.
    while True:
        # Placed here so that the screen is cleared and greets after
        # every choice.
        clear_screen()
        print("---Project Euler Solver---")
        print("Choose one of the following problems to solve:")
        # Go through the list of problems solved and remember possible
        # choices that a user can make.
        possible_choices = []
        for problem in all_problems:
            possible_choices.append(problem.number)
            # Print each possible choice along with the problem name.
            template = "{0}. {1}.".format(problem.number, problem.name)
            print(template)
        # Placed outside of the loop because exit is not a problem.
        print("\n0. Exit.")
        # Try to get a user to input a number. If it is anything other than a
        # number, it will raise an exception.
        try:
            choice = input("> ")
        except Exception:
            print("===INVALID CHOICE===")
            sleep(1)
            continue
        # If the user chooses 0 then exit the program.
        if choice == 0:
            print("------Ending program------")
            exit()
        # If the user's choice is in the list of possible choices,
        # then look up the problem and run it.
        elif choice in possible_choices:
            problem = problem_lookup(choice, all_problems)
            problem.show_info()
            problem.solve()
            input("Press enter to continue...")
        # Otherwise, re-run the loop till you get a correct input.
        else:
            print("===INVALID CHOICE===")
            sleep(1)
