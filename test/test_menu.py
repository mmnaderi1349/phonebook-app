from test_list import add_name, show_name, delete, edit
from test_storage import load

def menu():
   fehrest = load()
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
         add_name(fehrest)
      elif choice == "2":
         show_name(fehrest)
      elif choice == "3":
         delete(fehrest)    
      elif choice == "4":
         edit(fehrest)                
      elif choice == "5":
         break  