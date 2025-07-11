import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "film_lib.json")

def save_film(films):
   with open(FILENAME, 'w') as f:
     json.dump(films,f)

def load_film():
   global films
   try:
      with open(FILENAME, 'r') as f:
         return json.load(f)
   except FileNotFoundError:
      return[]  