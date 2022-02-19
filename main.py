from classes import *
from newuser import *
from login import *
from Main_Screen import *

def Enter_Screen():
    user = ""
    users = {}

    print("Welcome To Jamm Bank")
    user_input = input("New Users Press 'A'\n Login Press 'B'").upper()

    if user_input == "A":
        user = New_User(user)

        print(f"Here is your new Account Number: {user.account_num}. Please save it for your personal records")

        users[user.account_num] = user
        user_log = open("Users.txt","a")
        user_log.write(f"\n{users}")
        user_log.close()
    elif user_input == "B":
        print("Worked")

    Main_Screen(user)



Enter_Screen()

#TODO CONTINUE WORKING ON THE HOME SCREEN (WITHDRAWS/DEPOSITS)