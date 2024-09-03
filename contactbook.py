# Contact book program

# Dictionary to store contacts
contacts = {}

def add_contact(name, phone_number):
    """Add a contact to the contact book."""
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone_number
        print("Contact added successfully.")

def view_contacts():
    """Display all contacts in the contact book."""
    if contacts:
        print("\nContacts:")
        for name, phone_number in contacts.items():
            print(f"Name: {name}, Phone Number: {phone_number}")
    else:
        print("No contacts found.")

def delete_contact(name):
    """Delete a contact from the contact book."""
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            add_contact(name, phone_number)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter contact name to delete: ")
            delete_contact(name)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()