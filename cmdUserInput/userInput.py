"""
Module Contains methods to get user input to run a project.

Author: Austin
"""


def task_picker():
    print(
        """
        0. Exit.
        1. Print
        2. Load
        """
    )
    user_input = input("What task do you want to do? ")
    if user_input == "0":
        print("Good Buy")
        return
    elif user_input == "1":
        print("hello")
    elif user_input == "2":
        print("loading")
    else:
        print("please enter a valid nubmer.")

    task_picker()
