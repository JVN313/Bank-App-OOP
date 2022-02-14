from classes import *
from newuser import *
from login import *
user = ""

new = input("are you a new user?: ")
if new == "y":
    user = New_User(user)
    
print("login")
Login(user)
print(user)


#Work on home menu and bank functions