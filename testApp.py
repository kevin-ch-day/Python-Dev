# testApp.py
# kevin.ch.day@gmail.com
# updated: 3/6/2022

import os
from datetime import datetime

# script title
APP_TITLE = "Test Python Application"
APP_DESC = "Test Python Application"
APP_LAST_UPDATED = "3/6/2022"
APP_LAST_RUN = datetime.now().strftime("%d-%m-%Y %H:%M")

# main menu
def mainMenu():
    while True:
        os.system("cls")
        print("** Main Menu **")
        print("1) - Run")
        print("2) - About")
        print("0) - Exit")
    
        userChoice = promptUserMenuChoice()
        if userChoice == "0":
            exitApp()
        elif userChoice == "1":
            run()
        elif userChoice == "2":
            about()
        else:
            print("Invalid Option [!!]")
        # if
        
        os.system("pause")
    # while
# function

def promptUserMenuChoice():
    userChoice = ""
    inputValid = False
    
    while not inputValid:
        userChoice = input("\nChoice: ")
        if userChoice < "0" and userChoice > "2":
            print("Invalid Menu Choice [!!]")
            inputValid = False
        else:
            inputValid = True
        # if
    # while
    return userChoice
# function

def exitApp():
    print("\nThank you for using the application!")
    os.system("pause")
    os.system("cls")    
    exit()
# function

def run():
    pass
# function
        
def about():
    print("\n** About **")
    print(APP_TITLE)
    print(APP_DESC)
    print("Last updated: " + APP_LAST_UPDATED)
    print("Last run: " + APP_LAST_RUN)
# function

# main
mainMenu()
# script