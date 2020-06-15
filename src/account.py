class Account():

    def __init__(self, balance):
        self.balance = balance
        self.transactions = []

    def current_balance(self):
        return 0
    
    def transact(self, amount):
        self.transactions.append(amount)