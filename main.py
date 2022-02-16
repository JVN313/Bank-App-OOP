from classes import *
from newuser import *
from login import *

def Enter_Screen():
    user = ""
    users = {}

    print("Welcome To Jamm Bank")
    user_input = input("New Users Press 'A' \n Login Press 'B'").upper()

    if user_input == "A":
        user = New_User(user)

        print(f"Here is your new Account Number: {user.account_num}. Please save it for your personal records")

        users[user.account_num] = user
        user_log = open("Users.text","a")
        user_log.write(str(users))
        user_log.close()

        Login(user)
        print("worked")
        
    
    elif user_input == "B":
        print("worked")


def Main_Screen():
    pass


Enter_Screen()

#Work on home menu and bank functions