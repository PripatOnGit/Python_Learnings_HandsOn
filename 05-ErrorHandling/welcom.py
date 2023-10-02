"""
welcome.py
"""
import json

filename = 'userName.json' 
user = ''
# Check for a history file 
try:
    with open(filename, 'r') as r: 
        # Load the user's name from the history file 
        
        user = json.load(r)

except IOError as e: 
    print("First-time login")
    print(f"{e}")
    # If the user was found in the history file, welcome them back 
    
if user != "": 
    print("Welcome back, " + user + "!")
else: # If the history file doesn't exist, ask the user for their name
    name = input("Hello! What's your name? ") 
    print("Welcome, " + name + "!")
    # Save the user's name to the history file 
    try:
        with open(filename, 'w') as f: 
            json.dump(name, f)
    except IOError: 
        print("There was a problem writing to the history file.")