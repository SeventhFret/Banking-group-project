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
        self.balance  = 0
        self.transactions = [] # list of dictionaries like {'title':'Blabla','value':1234,'date':'17.03.2023'}

    def deposit(self):
        title = input("Description of your deposit: ")
        value = int(input("How much money would you like to deposit? "))
        transaction_date = datetime.datetime.now()
        self.balance += value
        self.transactions.append({'title':title,'value':value,'date':transaction_date})
        print(f"Deposit {value} euros was charged. Your balance now is: {self.balance} euros. Gratz")

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
        if len(self.transactions) > 0:
            for transaction in self.transactions:
                print(f"{transaction['date']} | {transaction['value']} | {transaction['title']}")
        else:
            print("You don't have any transactions.")
        print()


class User(BankAccount):
    accounts = []

    def __init__(self):
        self.user_account = {} 
        self.authorized = False

    def register(self):
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
                    self.user_account["Login"] = login
                    self.user_account["Password"] = password
                    return True
                else:
                    print("Password is wrong!")
                    sleep(2)
                    system('clear')
                    continue
        elif c.lower() == "n":
            print("Alright, then see you.")
            exit()

    def authorization(self):
        system('clear')
        if input('Type your login: ') == self.user_account["Login"]:
            if input("Type your password: ") == self.user_account["Password"]:
                self.authorized = True
                print("Authorized successful!")
            else:
                print("Wrong password for", self.user_account["Login"])
        else:
            print("Wrong login!")

    def create_bank_account(self):
        iban = "DE" + str(random.randint(10000000000000000000, 100000000000000000000))
        spaced = ' '.join([iban[i:i+4] for i in range(0, len(iban), 4)])
        print(spaced)
        super().__init__(spaced)


# Maksym
class Bank(User):
    def __init__(self):
        super().__init__()
        print("Welcome to bank!".center(50, '='))

        if "Login" not in self.user_account:
            self.register()
        else:
            self.authorization()
        
        self.create_bank_account()

        choice = True

        while choice != 'x':
            system('clear')
            choice = input("""Please, select an option:
            [1] - balance
            [2] - withdraw 
            [3] - deposit
            [x] - exit 
            """)

            if choice == "1":
                self.show_balance()
                
            elif choice == "2":
                self.withdraw()
            
            elif choice == "3":
                self.deposit()
                
            if choice == "x":
                print("Thank you for having used our bank and have a nice day!")
                quit()
            
            elif choice != "x":
                input("Press Enter to continue.")
                continue

bank = Bank()