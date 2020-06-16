class Account():

    def __init__(self, balance, TransactionClass, printer):
        self.balance = balance
        self.transactions = []
        self.TransactionClass = TransactionClass
        self.printer = printer

    def current_balance(self):
        return 0
    
    def transact(self, amount):
        transaction = self.TransactionClass(amount)
        self.transactions.append(transaction)
    
    def print_statement(self):
        statement = self.printer.print_statement(self.transactions)
        return statement
