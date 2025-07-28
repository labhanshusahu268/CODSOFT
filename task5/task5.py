contacts = []

a = int(input("Enter number of contacts you want to store in contact book: "))

for i in range(a):
    print(f"\nEnter details for contact {i+1}:")
    name = input("Name: ")
    contact = input("Contact Number: ")
    gmail = input("Gmail ID: ")
    address = input("Address: ")
    
    contact_entry = {
        "name": name,
        "contact": contact,
        "gmail": gmail,
        "address": address
    }
    contacts.append(contact_entry)

def show_details():
    if not contacts:
        print("Contact book is empty!")
        return
    for i, c in enumerate(contacts, 1):
        print(f"\nContact {i}:")
        print(f"Name    : {c['name']}")
        print(f"Contact : {c['contact']}")
        print(f"Gmail   : {c['gmail']}")
        print(f"Address : {c['address']}")

def searching():
    search = input("Enter name or contact to search: ")
    found = False
    for c in contacts:
        if c["name"] == search or c["contact"] == search:
            print("\nContact Found:")
            print(f"Name    : {c['name']}")
            print(f"Contact : {c['contact']}")
            print(f"Gmail   : {c['gmail']}")
            print(f"Address : {c['address']}")
            found = True
            break
    if not found:
        print("No matching contact found.")

def updating_details():
    search = input("Enter name of contact to update: ")
    for c in contacts:
        if c["name"] == search:
            print("\nWhich detail do you want to update?")
            print("1. Name\n2. Contact\n3. Gmail\n4. Address")
            choice = input("Enter choice number: ")

            if choice == "1":
                c["name"] = input("Enter new name: ")
            elif choice == "2":
                c["contact"] = input("Enter new contact number: ")
            elif choice == "3":
                c["gmail"] = input("Enter new Gmail ID: ")
            elif choice == "4":
                c["address"] = input("Enter new address: ")
            else:
                print("Invalid choice.")
            return
    print("Contact not found.")

def delete_details():
    search = input("Enter name of contact to delete: ")
    for c in contacts:
        if c["name"] == search:
            contacts.remove(c)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

while True:
    print("\n==== Contact Book Menu ====")
    print("1. Show All Contacts")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        show_details()
    elif choice == "2":
        searching()
    elif choice == "3":
        updating_details()
    elif choice == "4":
        delete_details()
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
