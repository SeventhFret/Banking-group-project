def deposit(self):
    title = input("Description of your deposit: ")
    value = int(input("How much money would you like to deposit? "))
    transaction_date = datetime.datetime.now()
    self.balance += value
    self.transactions.append({'title': title, 'value': value, 'date': transaction_date})