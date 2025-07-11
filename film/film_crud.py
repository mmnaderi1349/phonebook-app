from film_storage import save_film

def add_film(films) :
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
    save_film(films)

def edit_film(films):     
  try:
      show_film(films)
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
        save_film(films)
      else:
        print("Please input a valid number!")  

  except ValueError:
    print("Please input a value number")          
        

def show_film(films) :
   print("\n------ Films List --------")
   if not films:
      print("Not any film!")
      return
   for idx,c in enumerate(films, start=1):
     print(f"{idx} . {c['name']} - Genr: {c['Genr']} - {c['year']} - imdb rank: {c['imdb']}")
   print("--------------------------\n")     

def del_film(films):
   if not films:
      print("There isn't any film!")
      return
   show_film(films)
   n = int(input("Inter film's number that you want to delete: "))
   try:
      if 1 <= n <= (len(films)):
         deleted = films.pop(n-1)
         save_film(films)
         print(f"{deleted['name']} deleted")
   except ValueError:
      print("Input a valid data")       