from film_crud import add_film, del_film, edit_film, show_film
from film_storage import load_film

def main_menu() :
    films = load_film()
    while True:
        print("Main Menu")
        print("1. add ")
        print("2. show")
        print("3. delete")
        print("4. edit")
        print("5. exit")        
        
        choice = input("Your selection: ")
        if choice == "1":
          add_film(films)
        elif choice == "2":
          show_film(films)
        elif choice == "3":
          del_film(films)  
        elif choice == "4":
          edit_film(films)                   
        elif choice == "5":
          print("Exit")
          break
        else:
           print("Bad selection!")  
