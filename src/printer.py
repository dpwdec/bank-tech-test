class Printer():
    
    def print_statement(self, transactions):
        balance = 0
        statement = "date       || credit  || debit   || balance"

        for transaction in transactions:
            date_col = f"\n{transaction.get_formatted_date()} || "

            balance_value = "%.2f" % balance
            padding = " " * (7 - len(balance_value))
            balance_col = balance_value + padding
            input_cols = ""
            transaction_row = ""

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
            
            transaction_row = date_col + input_cols + balance_col
            statement += transaction_row
        
            balance += transaction.value

        return statement