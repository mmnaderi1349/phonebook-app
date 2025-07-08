import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "fortest.json")

def save(fehrest):
   with open(FILENAME, 'w') as f:
      json.dump(fehrest, f) 

def load():
   global fehrest
   try:
      with open(FILENAME, 'r') as f:
         return json.load(f)

   except FileNotFoundError:
      return []        