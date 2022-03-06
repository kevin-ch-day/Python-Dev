# testScript.py
# kevin.ch.day@gmail.com
# updated: 3/6/2022

import os

# script title
#print('** Test Python Script **')

# prompt for username
def promptUsername():
    username = input("\nEnter username: ")
    print("Hello, " + username.upper() + " !")
# function

def userInteraction1():
# prompt user, how do they feel?
    userfeeling = input("\nHow do you feel? ")
    if userfeeling == "Good":
        print("Great to hear!")
    elif userfeeling == "Bad":
        print("Hope you feel better :-)")
    else:
        print("nice!")
    # if
# function


# main
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print(now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d-%m-%Y %H:%M")
print(dt_string)	
# script