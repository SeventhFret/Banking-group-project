class Bank_account:
    
    def __init__(self, balance=float(input("Which is your initial balance? ")), interest:float=0.02):
        self.balance = balance
        self.interest_rate = interest
    
    def deposit(self):
        amount = float(input("How much money would you like to deposit? "))
        self.balance += amount
        self.balance = (self.balance) + self.balance * self.interest_rate
        return f"Your balance, included an interest of 0.02, is {self.balance:.2f}."
        
    def withdraw(self):
        amount = float(input("How much money would you like to withdraw? "))
        if amount > self.balance:
            return "I am sorry, but you do not have enough money."
        elif amount == self.balance:
            print(f"Attention, you have emptied your bank_account.") 
        self.balance -= amount
        return f"Your balance is {self.balance:.2f}."

my_bank = Bank_account()
print(my_bank.deposit())
print(my_bank.withdraw())