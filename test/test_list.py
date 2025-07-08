from test_storage import save

def add_name(list):
  name = input("name: ")
  lname = input("last name: ")
  names = {
     "name": name,
     "lname": lname
   }
  list.append(names)
  save(list)
  print("The new name added successfully") 

  def show_name(list):
   if not list:
      print("There isn't any name!")
      return
   print()
   print("----------------- LIST -------------------")
   for idx,c in enumerate(list, start=1):
       print(f"{idx}. {c['name']} - {c['lname']}")
   print("------------------------------------------")  
   print()  

def delete(list):
   show_name(list)
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
    except ValueError:fdg
       print("Error")        

def edit(list):
    show_name(list)
    if not list:
      return
    try:
      idx = int(input("Which the number do you want to edit: "))
      if 1 <= idx <= len(list):
         names = list[idx-1]
         name = input(f"Name {names['name']}:") or names["name"]
         lname = input(f"Name {names['lname']}:") or names["lname"]
         names.update({
         "name": name,
         "lname": lname
         })
         save(list)
         print(f"(({[name]} {[lname]})) edited")
      else:
         print("invalid number!!!")   
   except ValueError:
      print("Please input a valid number!")           
       


