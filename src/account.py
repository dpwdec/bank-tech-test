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
        if(len(self.transactions) > 0):
            statement = statement + "\n" + self.transactions[0].get_formatted_date() + " ||         || " + ("%.2f" % self.transactions[0].transaction_value) + " || 0.00"
            #statement = statement + "\n" + self.transactions[0].get_formatted_date() + "   " + str(self.transactions[0].transaction_value)
        return statement
