import json
import os

list = [ ]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "fortest.json")

def save():
   with open(FILENAME, 'w') as f:
      json.dump(list, f) 


def add_name():
  name = input("name: ")
  lname = input("last name: ")
  names = {
     "name": name,
     "lname": lname
   }
  list.append(names)
  save()
  print("The new name added successfully") 

def show_name():
   if not list:
      print("There isn't any name!")
      return
   print()
   print("----------------- LIST -------------------")
   for idx,c in enumerate(list, start=1):
       print(f"{idx}. {c['name']} - {c['lname']}")
   print("------------------------------------------")  
   print()  
       

def delete():
   show_name()
   if not list:
      print("There isn't any name!")
      return
   try:
      idx = int(input("Input the number for delete: "))
      if 1 <= idx <= (len(list)):
         deleted = list.pop(idx-1)
         print(f"(({deleted['name']})) deleted")
      else:
          print("Input valid number!")  
   except ValueError:
      print("Error")        
      
def load():
   global list
   try:
      with open(FILENAME, 'r') as f:
         list = json.load(f)

   except FileNotFoundError:
      list = []  

def edit():
   if not list:
      return
   try:
      show_name()
      idx = int(input("Which the number do you want to edit: "))
      if 1 <= idx <= len(list):
         names = list[idx-1]
         name = input(f"Name {names['name']}:") or names["name"]
         lname = input(f"Name {names['lname']}:") or names["lname"]
         names.update({
         "name": name,
         "lname": lname
         })
         save()
         print(f"(({[name]} {[lname]})) edited")
      else:
         print("invalid number!!!")   
   except ValueError:
      print("Please input a valid number!")           

def menu():
   while True:
      print("------ Main Menu -------")
      print("Input your choice: ")
      print("1. Add new name")
      print("2.Show All names")
      print("3. Delete")
      print("4. Edit")      
      print("5. Exit")      


      choice = input("Input your choice: ")
      if choice == "1":
         add_name()
      elif choice == "2":
         show_name()
      elif choice == "3":
         delete()    
      elif choice == "4":
         edit()                
      elif choice == "5":
         break  
load()
menu()         