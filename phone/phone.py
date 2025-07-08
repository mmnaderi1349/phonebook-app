import json
import os

# لیست مخاطبان
contacts = [ ]

# مسیر فولدر اسکریپت (دایرکتوری phone)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "contacts.json")

def save_contacts():
    with open(FILENAME, 'w') as f:
        json.dump(contacts, f)

def load_contacts():
    global contacts
    try:
        with open(FILENAME, 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []        

def add_contact():
    print("\n---------- Add new contact ----------")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts()   # ⭐️ این خط اضافه شد
    print("✅  Contact added successfully.\n")

def show_contacts():
    print("\n---------- Contacts list ----------") 
    if not contacts:
        print("There isn't any contact! ")
        return
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} - {c['phone']} - {c['email']} - {c['address']}")
    print()

def delete_contact():
    show_contacts()
    if not contacts:
        return
    try:
        idx = int(input("Enter the number of contact to delete: "))
        if 1 <= idx <= len(contacts):
            deleted = contacts.pop(idx - 1)
            save_contacts()
            print(f"✅ Deleted: {deleted['name']}")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Please enter a valid number.")    

def edit_contact():
    show_contacts()
    if not contacts:
        return
    try:
        idx = int(input("Enter the number of contact to edit: "))
        if 1 <= idx <= len(contacts):
            contact = contacts[idx - 1]
            print("\nLeave empty to keep current value.")

            new_name = input(f"Name [{contact['name']}]: ") or contact['name']
            new_phone = input(f"Phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"Email [{contact['email']}]: ") or contact['email']
            new_address = input(f"Address [{contact['address']}]: ") or contact['address']
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            save_contacts()
            print("✅ Contact updated successfully.\n")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Please enter a valid number.")



def main_menu():
    while True:
        print("🟢  Main Menu")
        print("1. Add new ")
        print("2. All contacts  ")
        print("3. Delete contact")
        print("4. Edit contact")
        print("5. Exit")        

        choice = input("Your choice : ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            delete_contact() 
        elif choice == "4":
            edit_contact()              
        elif choice == "5":
            print("Exit .")
            break          
        else:
            print("❌ Invalid choice!\n")

# اجرای برنامه
load_contacts()
main_menu()    