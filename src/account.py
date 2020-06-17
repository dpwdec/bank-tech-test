class Account():

    def __init__(self, TransactionClass, printer):
        self.transactions = []
        self.TransactionClass = TransactionClass
        self.printer = printer

    def deposit(self, amount):
        self._transact(abs(amount))

    def withdraw(self, amount):
        self._transact(-abs(amount))
    
    def print_statement(self):
        statement = self.printer.print_statement(self.transactions)
        return statement

    """ Private """
    def _transact(self, amount):
        transaction = self.TransactionClass(amount)
        self.transactions.append(transaction)
