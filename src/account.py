class Account():

    def __init__(self, TransactionClass, printer):
        self.transactions = []
        self.TransactionClass = TransactionClass
        self.printer = printer

    def deposit(self, amount):
        self.transact(amount)
    
    def transact(self, amount):
        transaction = self.TransactionClass(amount)
        self.transactions.append(transaction)
    
    def print_statement(self):
        statement = self.printer.print_statement(self.transactions)
        return statement
