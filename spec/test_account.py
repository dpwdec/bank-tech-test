from unittest import TestCase
from unittest import mock
from src.account import Account

class TestAccount(TestCase):

    def setUp(self):
        transaction_object = mock.Mock()
        TransactionClass = mock.Mock()
        TransactionClass.return_value = transaction_object
        self.account = Account(0, TransactionClass)

    def _has_list_of_transactions(self):
        pass
        #account = Account(0)
        #self.assertEqual(account.transactions, [])

    def test_execute_single_transaction(self):
        self.account.transact(200)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertIsInstance(self.account.transactions[0], mock.Mock)
    
    def test_execute_multiple_transactions(self):
        self.account.transact(200)
        self.account.transact(-200)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertIsInstance(self.account.transactions[0], mock.Mock)
        self.assertIsInstance(self.account.transactions[1], mock.Mock)
    
    def test_print_zero_line_statement(self):
        """
        If transactions is empty print only account history headers
        date       || credit  || debit  || balance
        """
        self.assertEqual(self.account.print_statement(), "date       || credit  || debit  || balance")
    
    def test_print_one_line_statement(self):
        """
        If transactions is contains one transaction for 200
        date       || credit  || debit  || balance
        14/01/2012 ||         || 200.00 || 0.00
        """
        statement =  "date       || credit  || debit  || balance\n14/01/2012 ||         || 200.00 || 0.00"
        positive_transaction = mock.Mock()
        positive_transaction.get_formatted_date.return_value = "14/01/2012"
        positive_transaction.is_debit.return_value = True
        positive_transaction.transaction_value = 200
        #self.assertEqual(positive_transaction.transaction_value, 200)
        self.account.transact(positive_transaction)
        self.assertEqual(self.account.print_statement(), statement)

    def test_returns_balance(self):
        self.assertEqual(self.account.current_balance(), 0)