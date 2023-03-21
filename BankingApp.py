import re
from os import system
from time import sleep
import datetime
import random

system('clear')

# Adrian
class BankAccount:
    def __init__(self, iban:str):
        self.status = 'green'
        self.red_limit = -200
        self.iban     = iban # this will be the "name" of the bank ccount
        self.balance  = 100
        self.transactions = [] # list of dictionaries like {'title':'Blabla','value':1234,'date':'17.03.2023'}

    def deposit(self):
        title = input("Description of your deposit: ")
        value = int(input("How much money would you like to deposit? "))
        transaction_date = datetime.datetime.now()
        self.balance += value
        self.transactions.append({'title':title,'value':value,'date':transaction_date})

    def withdraw(self):
        title = input("Description of your withdraw: ")
        value = int(input("How much money would you like to withdraw? "))
        transaction_date = datetime.datetime.now()
        if self.status != "red":
            self.balance -= value
            self.transactions.append({'title':title,'value':-value,'date':transaction_date})
        if self.balance < 0 and self.status != "red":
            print(f"You owe {self.balance} euros to the bank.")
            self.status = "red"
        elif self.status == "red":
            print(f"Sorry! You need to deposit more than {self.balance*-1} euros before...")
            
    def show_balance(self):
        print(f"Your balance is now: {self.balance} euros.")
        print(f"Until now you have this transactions done:")
        for transaction in self.transactions:
            print(f"{transaction['date']} | {transaction['value']} | {transaction['title']}")
        print()


class User(BankAccount):
    _user_account = {}
    accounts = []
    def __init__(self):
        self.authorized = False

    @classmethod
    def register(cls):
        print("Hello, dear user! Looks like you don't have an account in our bank yet.")
        c = input("Do you want to register?[Y/N] ")
        if c.lower() == "y":
            login = input("Create your username: ")
            while True:
                password = input("""Create your password: 
Password should contain:
    -> At least one digit [0-9]
    -> At least one lowercase character [a-z]
    -> At least one uppercase character [A-Z]
    -> At least one special character [#?!@$%^&*-]
    -> At least 8 characters in length, but no more than 32.
    """)
                pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
                if re.match(pattern, password) is not None:
                    print("Account successfully created!")
                    cls.user_account["Login"] = login
                    cls.user_account["Password"] = password
                    return True
                else:
                    print("Password is wrong!")
                    sleep(2)
                    system('clear')
                    continue
        elif c.lower() == "n":
            print("Alright, then see you.")
            exit()

    @classmethod
    def authorization(cls, self):
        system('clear')
        if input('Type your login: ') == cls._user_account["Login"]:
            if input("Type your password: ") == cls._user_account["Password"]:
                self.authorized = True
                print("Authorized successful!")
            else:
                print("Wrong password for", cls._user_account["Login"])
        else:
            print("Wrong login!")

    def create_bank_accout(self):
        iban = "DE" + str(random.randint(10000000000000000000, 100000000000000000000))
        super().__init__(iban)


# Maksym
class Bank(User):
    def __init__(self):
        self.authorized = False
        print("Welcome to bank!".center(50, '='))
        # if "Login" not in Bank._user_account:
        #     super().register()
        # else:
        #     self.authorization()

        super().create_bank_accout()
        print(super().balance)









bank = Bank()
