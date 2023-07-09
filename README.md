**Project Description:**

The Phone Directory is a console application developed by Zaid Ullah that allows users to manage their phone contacts efficiently. The application is implemented using the Object-Oriented Programming (OOP) concept in Python. It provides various features such as adding contacts, viewing the phone directory, updating contacts, deleting contacts, and simulating calls to contacts.

The project consists of two main classes: Contact and PhoneDirectory. The Contact class represents an individual contact with attributes like first name, last name, phone number, email address, address, and street. The class also defines a __str__ method to provide a string representation of a contact.

The PhoneDirectory class serves as the main driver for the application. It manages a list of contacts and provides methods for validating input data, loading contacts from a text file, saving contacts to the file, adding a new contact, viewing the phone directory, updating an existing contact, deleting a contact, and simulating calls to contacts.

The application utilizes the prettytable library to display the phone directory in a tabular format, enhancing the readability and presentation of contact information.

Upon running the program, users are greeted with a welcome message and a menu of options to choose from. They can interact with the application by entering their choices and providing the required information for each operation. The program validates the input data to ensure correctness and provides appropriate error messages in case of any issues.

The phone directory data is stored in a text file named "phone_directory.txt" in a comma-separated format. The data is loaded from the file at the start of the program and saved back to the file whenever changes are made to the contacts.

Overall, the Phone Directory project offers a user-friendly interface, data persistence through file handling, and essential contact management functionalities. It provides an organized and efficient way to store, view, update, and delete contacts, improving contact management for users.