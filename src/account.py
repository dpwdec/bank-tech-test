class Account():

    def __init__(self, balance):
        self.balance = balance
        self.transactions = []

    def current_balance(self):
        return 0
    
    def transact(self, transaction):
        self.transactions.append(transaction)
    
    def print_statement(self):
        statement = "date       || credit  || debit  || balance"
        return statement
