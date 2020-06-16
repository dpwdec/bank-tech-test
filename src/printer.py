class Printer():
    
    def print_statement(self, transactions):
        balance = 0
        balance_value = "%.2f" % balance
        padding = " " * (7 - len(balance_value))
        balance_col = balance_value + padding

        statement = "date       || credit  || debit   || balance"
        date_col = f"\n{transactions[0].get_formatted_date()} || "
        transacton_cols = ""

        if(transactions[0].is_debit()):
            credit_col = "        || "
            float_value = "%.2f" % transactions[0].value
            padding = " " * (8 - len(float_value))
            debit_col = f"{float_value}{padding}"
            transacton_cols = credit_col + debit_col + "|| "
        else:
            pass

        print("----- ")
        statement += date_col
        statement += transacton_cols
        statement += balance_col
        print(statement)
        return statement