# menu.py
from contacts import add_contact, show_contacts, delete_contact, edit_contact
from storage import load_contacts

def main_menu():
    contacts = load_contacts()
    while True:
        print("\n🟢 منوی اصلی")
        print("1. افزودن مخاطب")
        print("2. نمایش همه مخاطبان")
        print("3. حذف مخاطب")
        print("4. ویرایش مخاطب")
        print("5. خروج")

        choice = input("انتخاب شما: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            print("👋 خداحافظ!")
            break
        else:
            print("❌ انتخاب نامعتبر!")