# contacts.py
from storage import save_contacts

def add_contact(contacts):
    print("\n---------- افزودن مخاطب ----------")
    name = input("نام: ")
    phone = input("شماره تلفن: ")
    email = input("ایمیل: ")
    address = input("آدرس: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("✅ مخاطب با موفقیت اضافه شد.\n")


def show_contacts(contacts):
    print("\n---------- لیست مخاطبان ----------")
    if not contacts:
        print("هیچ مخاطبی وجود ندارد!")
        return
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} - {c['phone']} - {c['email']} - {c['address']}")
    print()


def delete_contact(contacts):
    show_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("شماره مخاطب برای حذف: "))
        if 1 <= idx <= len(contacts):
            deleted = contacts.pop(idx - 1)
            save_contacts(contacts)
            print(f"✅ حذف شد: {deleted['name']}")
        else:
            print("❌ شماره نامعتبر!")
    except ValueError:
        print("❌ لطفا یک عدد معتبر وارد کنید.")


def edit_contact(contacts):
    show_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("شماره مخاطب برای ویرایش: "))
        if 1 <= idx <= len(contacts):
            contact = contacts[idx - 1]
            print("\nبرای حفظ مقدار قبلی، خالی بگذارید.")

            new_name = input(f"نام [{contact['name']}]: ") or contact['name']
            new_phone = input(f"شماره تلفن [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"ایمیل [{contact['email']}]: ") or contact['email']
            new_address = input(f"آدرس [{contact['address']}]: ") or contact['address']
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            save_contacts(contacts)
            print("✅ مخاطب با موفقیت ویرایش شد.\n")
        else:
            print("❌ شماره نامعتبر!")
    except ValueError:
        print("❌ لطفا یک عدد معتبر وارد کنید.")