from classes import *

def New_User(user):
    user = User(input("Enter Name: "), int(input("Enter Age: ")), input("Enter Sex: "), int(input("Enter A 4 digit Pin: ")))
    return user
