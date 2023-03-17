


class BankAccount:
    def __init__(self, iban:str, total=0, status='white'):
        self.iban     = iban
        self.total    = total
        self.status   = status
        self.deposits = [] # list of dictionaries like {'title':'Blabla','value':1234,'date':'17.03.2023'}
        self.withdraws = [] # list of dictionaries like {'title':'Blabla','value':1234,'date':'17.03.2023'}

    def turn_off(self):
        pass


# Maksym
class Bank(BankAccount):
    accounts = []
    def __init__(self):
        pass

    @classmethod
    def create_account(self):
        pass