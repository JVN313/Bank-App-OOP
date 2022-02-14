import random

class User():

    def __init__(self, name, age, sex, pin):
        self.name = name
        self.age = age
        self.sex = sex
        self.account_num = random.randint(0, 10000)
        self.pin = pin

    def __repr__(self):
        return f'User("{self.name}", "{self.age}", "{self.sex}", "{self.account_num}")'
     

class Bank():
    pass