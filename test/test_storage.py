import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "fortest.json")

def save(list):
   with open(FILENAME, 'w') as f:
      json.dump(list, f) 

def load():
   global list
   try:
      with open(FILENAME, 'r') as f:
         list = json.load(f)

   except FileNotFoundError:
      return []        