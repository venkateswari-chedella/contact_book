import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts()
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("\nName:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


contacts = load_contacts()

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")