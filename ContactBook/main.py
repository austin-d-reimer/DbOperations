"""
Module Contains methods to get user input to run a project.

Author: Austin
"""
from contact import Contact

contact = Contact()


def task_picker():
    print(
        """
        0. Exit.
        1. Print contact.
        2. Enter new contact.
        """
    )
    user_input = input("What task do you want to do? ")
    if user_input == "0":
        print("Good Bye")
        return
    elif user_input == "1":
        contact.read_contact()
    elif user_input == "2":
        print("Enter new Contact.")
        contact.add_contact()
    else:
        print("please enter a valid nubmer.")

    task_picker()


task_picker()