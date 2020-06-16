class Printer():
    
    def print_statement(self, transactions):
        balance = 0
        statement = "date       || credit  || debit   || balance"

        for transaction in transactions:
            statement += (self._format_date_col(transaction) + self._format_debit_credit_cols(transaction) + self._format_balance_col(balance))
            balance += transaction.value

        return statement
    
    def _format_date_col(self, transaction):
        return f"\n{transaction.get_formatted_date()} || "

    def _format_debit_credit_cols(self, transaction):
        value_col = "%.2f" % abs(transaction.value)
        padding = " " * (8 - len(value_col))

        if transaction.is_debit(): return "        || " + value_col + padding + "|| "
        return value_col + padding + "|| " + "        || "
    
    def _format_balance_col(self, balance):
        balance_str = "%.2f" % balance
        return "%.2f" % balance + (" " * (7 - len(balance_str)))
    

