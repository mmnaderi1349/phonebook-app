# storage.py
import json
import os

# تعیین مسیر مطلق فایل JSON (در کنار فایل‌های پروژه)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "contacts.json")

def save_contacts(contacts):  
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def load_contacts():
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []