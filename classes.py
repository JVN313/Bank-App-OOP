import random

class Bank():
    
    def __init__(self):
        self.account_balance = 0

    def Withdraw(self, amount):
        self.account_balance = self.account_balance - amount
        return self.account_balance

    def Deposit(self, amount):
        self.account_balance = self.account_balance + amount
        return self.account_balance


class User(Bank):

    def __init__(self, name, age, sex, pin):
        super().__init__()
        self.name = name
        self.age = age
        self.sex = sex
        self.account_num = random.randint(0, 10000)
        self.pin = pin

    def __repr__(self):
        return f'{self.name}("{self.age}", "{self.sex}", "{self.account_num}")'
     
