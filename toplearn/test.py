# لیست مخاطبان
contacts = [ ]

def add_contact() :
    print("\n---------- افزودن مخاطب جدید ----------")
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
    print("✅ مخاطب با موفقیت اضافه شد.\n")

def show_contacts():
    print("\n---------- لیست مخاطبان ----------") 
    if not contacts:
      print("هنوز مخاطبی ثبت نشده است")
      return
    for idx, c in enumerate(contacts, start=1):
       print(f"{idx}. {c['name']} - {c['phone']} - {c['email']} - {c['address']}")
    print()
def main_menu():
    while True:
        print("🟢 منو اصلی")
        print("1. افزودن مخاطب")
        print("2. نمایش همه مخاطبان")
        print("3. خروج")

        choice = input("انتخاب شما: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            print("خروج از برنامه.")
            break
        else:
            print("❌ انتخاب نامعتبر!\n")

# اجرای برنامه
main_menu()    

