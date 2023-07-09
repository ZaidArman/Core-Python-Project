import re
from prettytable import PrettyTable

CONTACTS_FILE = r"C:\Users\zaid arman\Desktop\Core Python Project\contact_list.txt"

class Contact:
    def __init__(self, first_name, last_name, phone_number, email, address, street):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.street = street

    def __str__(self):
        return f"Contact: {self.first_name} {self.last_name}"

class PhoneDirectory:
    def __init__(self):
        self.contacts = []

    def validate_name(self, name):
        if not name.isalpha():
            raise ValueError("Invalid name. Only alphabetic characters are allowed.")

    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address.")

    def validate_integer(self, number):
        if not number.isdigit():
            raise ValueError("Invalid number. Only integer values are allowed.")

    def load_contacts(self):
        try:
            with open(CONTACTS_FILE, "r") as file:
                for line in file:
                    contact_data = line.strip().split(",")
                    first_name = contact_data[0]
                    last_name = contact_data[1]
                    email = contact_data[2]
                    address = contact_data[3]
                    street = int(contact_data[4])
                    phone_number = int(contact_data[5])

                    contact = Contact(first_name, last_name, phone_number, email, address, street)
                    self.contacts.append(contact)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty phone directory
            self.contacts = []

    def save_contacts(self):
        with open(CONTACTS_FILE, "w") as file:
            for contact in self.contacts:
                file.write(
                    f"{contact.first_name},{contact.last_name},{contact.email},{contact.address},{contact.street},{contact.phone_number}\n"
                )

    def add_contact(self):
        print("Phone Directory")
        print("------------------------")
        try:
            first_name = input("Enter first name: ")
            self.validate_name(first_name)

            last_name = input("Enter last name: ")
            self.validate_name(last_name)

            phone_number = input("Enter phone number: ")
            self.validate_integer(phone_number)

            email = input("Enter email address: ")
            self.validate_email(email)

            address = input("Enter address: ")

            street = input("Enter street Number: ")
            self.validate_integer(street)

            contact = Contact(first_name, last_name, int(phone_number), email, address, int(street))
            self.contacts.append(contact)

            self.save_contacts()

            print("Contact added successfully!")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def view_directory(self):
        print("View Phone Directory")
        print("------------------------")

        if len(self.contacts) == 0:
            print("Phone directory is empty.")
        else:
            table = PrettyTable()
            table.field_names = ["First Name", "Last Name", "Email", "Address", "Street", "Phone Number"]

            for contact in self.contacts:
                table.add_row(
                    [contact.first_name, contact.last_name, contact.email, contact.address, contact.street, contact.phone_number]
                )

                # Add spacing between contacts
                table.add_row(["", "", "", "", "", ""])

            # Remove the last empty row
            table.del_row(-1)

            print(table)

    def update_contact(self):
        print("Update Phone Directory")
        print("------------------------")
        first_name = input("Enter first name of the contact to update: ")

        contact_found = False
        for contact in self.contacts:
            if contact.first_name == first_name:
                contact_found = True
                print("Contact Information:")
                print("------------------------")
                print(f"First Name: {contact.first_name}")
                print(f"Last Name: {contact.last_name}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print(f"Street: {contact.street}")
                print(f"Phone Number: {contact.phone_number}")
                print("------------------------")

                try:
                    last_name = input("Enter last name: ")
                    self.validate_name(last_name)

                    email = input("Enter email address: ")
                    self.validate_email(email)

                    address = input("Enter location address: ")

                    street = input("Enter street address: ")
                    self.validate_integer(street)

                    phone_number = input("Enter phone number: ")
                    self.validate_integer(phone_number)

                    contact.last_name = last_name
                    contact.email = email
                    contact.address = address
                    contact.street = int(street)
                    contact.phone_number = int(phone_number)

                    self.save_contacts()

                    print("Contact updated successfully!")
                except ValueError as e:
                    print(f"Error: {str(e)}")

                break

        if not contact_found:
            print("Contact not found.")

    def delete_contact(self):
        print("Delete Contact")
        print("------------------------")
        first_name = input("Enter first name of the contact to delete: ")

        contact_found = False
        for contact in self.contacts:
            if contact.first_name == first_name:
                contact_found = True
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted successfully!")
                break

        if not contact_found:
            print("Contact not found.")

    def call_contact(self):
        print("Call Contact")
        print("------------------------")
        first_name = input("Enter first name of the contact to call: ")

        contact_found = False
        for contact in self.contacts:
            if contact.first_name == first_name:
                contact_found = True
                print(f"Calling To {contact.first_name}...")
                break

        if not contact_found:
            print("Contact not found.")

    def phone_directory_program(self):
        print("Welcome to the Phone Directory!")
        print("------------------------")

        self.load_contacts()

        while True:
            print("Menu:")
            print("1. Add Contact")
            print("2. View Phone Directory")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Call Contact")
            print("0. Exit")
            print("------------------------")

            choice = input("Enter your choice: ")

            if choice == "0":
                print("Thank you for using the Phone Directory!")
                break
            elif choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_directory()
            elif choice == "3":
                self.update_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.call_contact()
            else:
                print("Invalid choice!")

            print()

phone_directory = PhoneDirectory()
phone_directory.phone_directory_program()