from test_storage import save

def add_name(fehrest):
  name = input("name: ")
  lname = input("last name: ")
  names = {
     "name": name,
     "lname": lname
   }
  fehrest.append(names)
  save(fehrest)
  print("The new name added successfully") 

def show_name(fehrest):
  if not fehrest:
     print("There isn't any name!")
     return
  print()
  print("----------------- fehrest -------------------")
  for idx,c in enumerate(fehrest, start=1):  
      print(f"{idx}. {c['name']} - {c['lname']}")
  print("------------------------------------------")  
  print()  

def delete(fehrest):
    show_name(fehrest)
    if not fehrest:
      print("There isn't any name!")
      return
    try:
       idx = int(input("Input the number for delete: "))
       if 1 <= idx <= (len(fehrest)):
          deleted = fehrest.pop(idx-1)
          save(fehrest)
          print(f"(({deleted['name']})) deleted")
       else:
            print("Input valid number!")  
    except ValueError:
          print("Error")        

def edit(fehrest):
    show_name(fehrest)
    if not fehrest:
       return
    try:
      idx = int(input("Which the number do you want to edit: "))
      if 1 <= idx <= len(fehrest):
         names = fehrest[idx-1]
         name = input(f"Name {names['name']}:") or names["name"]
         lname = input(f"Name {names['lname']}:") or names["lname"]
         names.update({
         "name": name,
         "lname": lname
         })
         save(fehrest)
         print(f"(({[name]} {[lname]})) edited")
      else:
         print("invalid number!!!")   
    except ValueError:
      print("Please input a valid number!")           
       


