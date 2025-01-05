import os

# Contact dictionary
contacts = {
    "Yasin": 51653216,
    "Nesli": 65622148
}

# To access dictionary:
# contacts["key"]
# contacts.get("key")
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts.update({name: phone})
    print(f"{name} has been added to the contacts.")

def search_contact():
    name = input("Name: ").lower()
    for contact_name, phone in contacts.items():
        if contact_name.lower() == name:
            print(phone)
            return
    else:
        print(f"No contact found with the name {name}.")

def delete_contact():
    name = input("Name: ")
    if name in contacts:
        contacts.pop(name)
        print(f"{name} has been removed from the contacts.")
        print(contacts)
    else:
        print("No such contact exists.")

def list_contacts():
    print("Name - Phone")
    for name in contacts:
        print(name, contacts.get(name))
    print(f"{len(contacts)} contact(s) listed.")

while True:
    os.system("cls")  # For clearing the terminal (use 'clear' if on Linux/MacOS)
    print("""
    Contact Manager
    Add       - 1
    Search    - 2
    Delete    - 3
    List      - 4
    """)
    choice = input("Select an option: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        list_contacts()

    input("Press Enter to continue...")
