"""
This Module Contains the methods to add a contact and retrieve a contact.

Author: Austin
"""
from DbOperations import DBOperations


class Contact:
    def __init__(self):
        self.db = DBOperations()
        self.db.create_DB()

    def add_contact(self):
        name = input("Contact Name: ")
        phoneNumber = input("Phone Number: ")

        self.db.add_contact(name, phoneNumber)

    def read_contact(self):
        print(
            """
        0. Exit.
        1. Print all contacts
        2. Search for Contact.
        """
        )
        user_input = input("What do you want to do? ")
        contacts = []
        if user_input == "0":
            return
        elif user_input == "1":
            contacts = self.db.read_from_db()

        for contact in contacts:
            print(contact)

        self.read_contact()
