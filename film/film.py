#film 
films = [ ]

def add_film() :
    print("/n------film-list-------")
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

def show_film() :
   print("------ Films List --------")
   if not films:
      print("Not any film!")
      return
   for n,c in films:
     print(f"{n} . {c['name']} - Genr: {c['Genr']} - {c['year']} - imdb rank: {c['imdb']}")
   print()     

def main_menu() :
    while True:
        print("Main Menu")
        print("1. add ")
        print("2. show")
        print("3. exit")
        
        choice = input("Your selection: ")
        if choice == "1":
          add_film()
        elif choice == "2":
          show_film()
        elif choice == "3":
          print("Exit")
          break
        else:
           print("Bad selection!")  

# Run! 
main_menu()           