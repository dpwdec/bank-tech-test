class Printer():
    
    def print_statement(self):
        pass

    # def test_print_zero_line_statement(self):
    #     """
    #     If transactions is empty print only account history headers
    #     date       || credit  || debit  || balance
    #     """
    #     self.assertEqual(self.account.print_statement(), "date       || credit  || debit  || balance")
    
    # def test_print_one_line_statement(self):
    #     """
    #     If transactions is contains one transaction for 200
    #     date       || credit  || debit  || balance
    #     14/01/2012 ||         || 200.00 || 0.00
    #     """
    #     statement =  "date       || credit  || debit  || balance\n14/01/2012 ||         || 200.00 || 0.00"
    #     positive_transaction = mock.Mock()
    #     positive_transaction.get_formatted_date.return_value = "14/01/2012"
    #     positive_transaction.is_debit.return_value = True
    #     positive_transaction.transaction_value = 200
    #     #self.assertEqual(positive_transaction.transaction_value, 200)
    #     self.account.transact(positive_transaction)
    #     self.assertEqual(self.account.print_statement(), statement)