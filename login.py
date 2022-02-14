from classes import *

def Login(user):
    attemps = 0

    while attemps <= 2:
        log = int(input("Enter Pin Number: "))

        if log != user.pin:
            print("No Pin Found")
            attemps += 1
            
        else:
            break

    if attemps == 3:
        print("Sorry to many failed atempts. Exiting Program")
        quit()

    return user