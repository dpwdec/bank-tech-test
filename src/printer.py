class Printer():
    
    def print_statement(self, transactions):
        balance = 0
        statement = "date       || credit  || debit   || balance"

        for transaction in transactions:
            transaction_row = self._format_date_col(transaction) + self._format_debit_credit_cols(transaction) + self._format_balance_col(balance)
            statement += transaction_row
            balance += transaction.value

        return statement
    
    def _format_date_col(self, transaction):
        return f"\n{transaction.get_formatted_date()} || "

    def _format_debit_credit_cols(self, transaction):
        input_cols = ""
        if(transaction.is_debit()):
            credit_col = "        || "
            float_value = "%.2f" % transaction.value
            padding = " " * (8 - len(float_value))
            debit_col = f"{float_value}{padding}"
            input_cols = credit_col + debit_col + "|| "
        else:
            debit_col = "        || "
            float_value = "%.2f" % abs(transaction.value)
            padding = " " * (8 - len(float_value))
            credit_col = f"{float_value}{padding}"
            input_cols = credit_col + "|| " + debit_col
        
        return input_cols
    
    def _format_balance_col(self, balance):
        balance_str = "%.2f" % balance
        return "%.2f" % balance + (" " * (7 - len(balance_str)))
    

