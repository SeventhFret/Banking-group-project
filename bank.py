class Bank_account:
    
    def __init__(self):
        self.balance = 0.0
    
    def deposit(self):
        amount = float(input("How much money would you like to deposit? "))
        self.balance += amount
        return f"Your balance is {self.balance:.2f}."
        
    def withdraw(self):
        amount = float(input("How much money would you like to withdraw? "))
        if amount > self.balance:
            return "I am sorry, but you do not have enough money."
        elif amount == self.balance:
            print(f"Attention, you have emptied your bank_account.") 
        self.balance -= amount
        return f"Your balance is {self.balance:.2f}."
    
    def check_balance(self):
        return f"Your balance is {self.balance:.2f}."

my_bank = Bank_account()
print(my_bank.deposit())
print(my_bank.withdraw())
print(my_bank.check_balance())