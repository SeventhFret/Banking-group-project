import re
from os import system
from time import sleep

system('clear')

class BankAccount:
    pass


# Maksym
class Bank(BankAccount):
    user_account = {}
    accounts = []
    def __init__(self):
        self.authorized = False
        print("Welcome to bank!")
        if "Login" not in Bank.user_account:
            self.register()
        else:
            self.authorization()


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
        else:
            print("Alright, then see you.")
            exit()



    @classmethod
    def authorization(cls, self):
        system('clear')
        if input('Type your login: ') == cls.user_account["Login"]:
            if input("Type your password: ") == cls.user_account["Password"]:
                self.authorized = True
                print("Authorized successful!")
        else:
            print("Wrong login!")
    

    @classmethod
    def create_account(self):
        super().__init__()


bank = Bank()
