#film 
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "film_lib.json")

films = [ ]

def add_film() :
    print("\n------film-list-------")
    name = input("Film name: ")
    Genr = input("Genr: ")
    year = input("Year: ")
    imdb = input("imdb:")

    film = {
      "name": name,
      "Genr": Genr,
      "year": year,
      "imdb": imdb
     }    
    films.append(film)
    print("The film added successfully!")
    save_film()

def save_film():
   with open(FILENAME, 'w') as f:
     json.dump(films,f)

def load_film():
   global films
   try:
      with open(FILENAME, 'r') as f:
         films = json.load(f)
   except FileNotFoundError:
      return[]        
       
def edit_film():     
  try:
      show_film()
      m = int(input("Which the number you want to edit: "))
      if 1 <= m <= (len(films)):
        film = films[m - 1]
        print("If no need to edit let it Empty and go to next!")
        new_name = input(f"name: [{film['name']}] ") or film['name'] 
        new_Genr = input(f"Genr: [{film['Genr']}] ") or film['Genr']
        new_year = input(f"year: [{film['year']}] ") or film['year']
        new_imdb = input(f"imdb: [{film['imdb']}] ") or film['imdb']
        film.update ({
          "name": new_name,
          "Genr": new_Genr,
          "year": new_year,
          "imdb": new_imdb
        }) 
        save_film()
      else:
        print("Please input a valid number!")  

  except ValueError:
    print("Please input a value number")          
        

def show_film() :
   print("\n------ Films List --------")
   if not films:
      print("Not any film!")
      return
   for idx,c in enumerate(films, start=1):
     print(f"{idx} . {c['name']} - Genr: {c['Genr']} - {c['year']} - imdb rank: {c['imdb']}")
   print("--------------------------\n")     

def del_film():
   if not films:
      print("There isn't any film!")
      return
   show_film()
   n = int(input("Inter film's number that you want to delete: "))
   try:
      if 1 <= n <= (len(films)):
         deleted = films.pop(n-1)
         save_film()
         print(f"{deleted['name']} deleted")
   except ValueError:
      print("Input a valid data")   

def main_menu() :
    while True:
        print("Main Menu")
        print("1. add ")
        print("2. show")
        print("3. delete")
        print("4. edit")
        print("5. exit")        
        
        choice = input("Your selection: ")
        if choice == "1":
          add_film()
        elif choice == "2":
          show_film()
        elif choice == "3":
          del_film()  
        elif choice == "4":
          edit_film()                   
        elif choice == "5":
          print("Exit")
          break
        else:
           print("Bad selection!")  

# Run!
load_film()
main_menu()           