import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts):
                print(f"Contact {i+1}:")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print()

    def edit_contact(self, index, name=None, phone=None, email=None):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact index.")
            return

        contact = self.contacts[index - 1]
        if name:
            contact.name = name
        if phone:
            contact.phone = phone
        if email:
            contact.email = email

    def delete_contact(self, index):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact index.")
            return

        del self.contacts[index - 1]

    def save_contacts(self, filename):
        with open(filename, 'w') as file:
            json.dump([vars(contact) for contact in self.contacts], file)

    def load_contacts(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.contacts = [Contact(**contact) for contact in data]

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Load Contacts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            index = int(input("Enter index of contact to edit: "))
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            contact_manager.edit_contact(index, name, phone, email)
        elif choice == '4':
            index = int(input("Enter index of contact to delete: "))
            contact_manager.delete_contact(index)
        elif choice == '5':
            filename = input("Enter filename to save contacts: ")
            contact_manager.save_contacts(filename)
        elif choice == '6':
            filename = input("Enter filename to load contacts: ")
            contact_manager.load_contacts(filename)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()