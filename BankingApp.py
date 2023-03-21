import re
from os import system
from time import sleep
from stringcolor import cs
import datetime
import random

system("clear")

# Adrian
class BankAccount:
    def __init__(self, iban: str):
        self.status = "green"
        self.red_limit = -200
        self.iban = iban  # this will be the "name" of the bank ccount
        self.balance = 0
        self.transactions = (
            []
        )  # list of dictionaries like {'title':'Blabla','value':1234,'date':'17.03.2023'}

    def deposit(self):
        value = int(input(cs("How much money would you like to deposit? ", "SkyBlue2")))
        title = input(cs("Description of your deposit: ", "SkyBlue2"))
        transaction_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.balance += value
        self.transactions.append(
            {"title": title, "value": value, "date": transaction_date}
        )
        print(
            cs(f"Deposit {value} euros was charged. Your balance now is: {self.balance} euros.", "green").bold()
        )

    def withdraw(self):
        value = int(input(cs("How much money would you like to withdraw? ", "SkyBlue2")))
        title = input(cs("Description of your withdraw: ", "SkyBlue2"))
        transaction_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.status != "red":
            if self.balance - value > self.red_limit:
                self.balance -= value
                self.transactions.append(
                    {"title": title, "value": -value, "date": transaction_date}
                )
            else:
                print(cs(f"Sorry! The red limit is {self.red_limit} euros.", "red").bold())
        if self.balance < 0 and self.status != "red":
            print(cs(f"You owe {self.balance} euros to the bank.", "Orange").bold())
            self.status = "red"
        elif self.status == "red":
            print(
                cs(f"Sorry! You need to deposit more than {self.balance*-1} euros before...", "red").bold()
            )

    def show_balance(self):
        print(f"Your balance is now: {self.balance} euros.")
        
    
    def statement(self):
        if len(self.transactions) > 0:
            print(f"Until now you have this transactions done:")
            for transaction in self.transactions:
                print(
                    f"{transaction['date']} | {transaction['value']} | {transaction['title']}"
                )
        else:
            print("You don't have any transactions.")
        print()


class User(BankAccount):
    accounts = []

    def __init__(self):
        self.user_account = {}
        self.authorized = False

    def register(self):
        print(cs("Hello, dear user! Looks like you don't have an account in our bank yet.", 'DeepSkyBlue3'))
        c = input("Do you want to register?[Y/N] ")
        if c.lower() == "y":
            login = input("Create your username: ")
            while True:
                password = input(
                    """Create your password: 
Password should contain:
    -> At least one digit [0-9]
    -> At least one lowercase character [a-z]
    -> At least one uppercase character [A-Z]
    -> At least one special character [#?!@$%^&*-]
    -> At least 8 characters in length, but no more than 32.
    """
                )
                pattern = (
                    "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
                )
                if re.match(pattern, password) is not None:
                    print(cs("Account successfully created!", "green").bold())
                    self.user_account["Login"] = login
                    self.user_account["Password"] = password
                    return True
                else:
                    print(cs("Password is wrong!", "red").bold())
                    sleep(2)
                    system("clear")
                    continue
        elif c.lower() == "n":
            print(cs("Alright, then see you.", "RoyalBlue"))
            exit()

    def authorization(self):
        system("clear")
        if input("Type your login: ") == self.user_account["Login"]:
            if input("Type your password: ") == self.user_account["Password"]:
                self.authorized = True
                print("Authorized successful!")
            else:
                print("Wrong password for", self.user_account["Login"])
        else:
            print("Wrong login!")

    def create_bank_account(self):
        iban = "DE" + str(random.randint(10000000000000000000, 100000000000000000000))
        spaced = " ".join([iban[i : i + 4] for i in range(0, len(iban), 4)])
        print(f"Your IBAN is {spaced}.")
        super().__init__(spaced)
        input("Press Enter to continue.")


# Maksym
class Bank(User):
    def __init__(self):
        super().__init__()
        print(cs("Welcome to bank!".center(50, "="), 'RoyalBlue'))

        if "Login" not in self.user_account:
            self.register()
        else:
            self.authorization()

        self.create_bank_account()

        choice = True

        while choice != "x":
            system("clear")
            choice = input(
                cs("""Please, select an option:
            [1] - balance
            [2] - withdraw 
            [3] - deposit
            [4] - statement
            [x] - exit 
            """
            , "RoyalBlue"))

            if choice == "1":
                self.show_balance()

            elif choice == "2":
                self.withdraw()

            elif choice == "3":
                self.deposit()
            
            elif choice == "4":
                self.statement()

            if choice == "x":
                print(
                    cs("We thank you for having used our banking services.\nWe wish a nice day!", "RoyalBlue")
                )
                quit()

            elif choice != "x":
                input("Press Enter to continue.")
                continue


bank = Bank()
