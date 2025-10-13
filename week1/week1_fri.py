import os
import re
import json

file_name = "phonebook.json"
phdDictionary = {}

def load_phonebook():
    global phdDictionary
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                phdDictionary = json.load(file)
        except:
            phdDictionary = {}
    else:
        phdDictionary = {}

def save_phonebook():
    with open(file_name, "w") as file:
        json.dump(phdDictionary, file, indent=4)


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def validate_phone(phone):
    pattern = r'^(\+?\d{1,3}[- ]?)?\d{10}$'
    return bool(re.match(pattern, phone))


def add_contact():
    load_phonebook()
    name = input("Enter Name: ")
    while True:
        email = input("Enter Email: ")
        if validate_email(email):
            break
        print("Invalid email format !!")
    while True:
        phone = input("Enter Phone: ")
        if validate_phone(phone):
            break
        print("Enter the correct phone number !!")
    phdDictionary[name] = {"Name": name, "Email": email, "Phone": phone}
    save_phonebook()
    print("Contact added successfully")

def show_contact():
    load_phonebook()
    if not phdDictionary:
        print("Phonebook is empty, add new contact !!!")
        return
    for contact in phdDictionary.values():
        print(f"Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}")

def search_contact():
    load_phonebook()
    name = input("Enter name to search: ")
    if name in phdDictionary:
        c = phdDictionary[name]
        print(f"Found: Name: {c['Name']}, Email: {c['Email']}, Phone: {c['Phone']}")
    else:
        print("Contact not found!")

def update_contact():
    load_phonebook()
    name = input("Enter name to update: ")
    if name in phdDictionary:
        print("Leave field blank to keep old value.")
        new_email = input(f"New Email (old: {phdDictionary[name]['Email']}): ") or phdDictionary[name]['Email']
        new_phone = input(f"New Phone (old: {phdDictionary[name]['Phone']}): ") or phdDictionary[name]['Phone']
        if validate_email(new_email) and validate_phone(new_phone):
            phdDictionary[name]["Email"] = new_email
            phdDictionary[name]["Phone"] = new_phone
            save_phonebook()
            print(f"Contact '{name}' updated successfully!")
        else:
            print("Invalid email or phone. Update failed.")
    else:
        print("Contact not found!")

def delete_contact():
    load_phonebook()
    name = input("Enter name to delete: ")
    if name in phdDictionary:
        confirm = input(f"are you sure you want to delete '{name}'? (yes/no): ")
        if confirm.lower() == "yes":
            del phdDictionary[name]
            save_phonebook()
            print(f"Contact '{name}' deleted !!")
        else:
            print("Delete cancelled.")
    else:
        print("Contact not found")

def main():
    while True:
        print("1. add Contact")
        print("2. Show all Contacts")
        print("3. search contact")
        print("4. update Contact")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exit")
            break
        else:
            print("Invalid choice.Please select between 1 to 6.")

main()
