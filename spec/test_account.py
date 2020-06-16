from unittest import TestCase
from unittest import mock
from src.account import Account

class TestAccount(TestCase):

    def setUp(self):
        transaction_object = mock.Mock()
        self.TransactionClass = mock.Mock()
        self.TransactionClass.return_value = transaction_object
        self.printer_mock = mock.Mock()
        self.printer_mock.print_statement.return_value = ""
        self.account = Account(0, self.TransactionClass, self.printer_mock)

    def _has_list_of_transactions(self):
        self.assertEqual(self.account.transactions, [])

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
    
    def test_transact_calls_transaction_class(self):
        self.account.transact(200)
        self.TransactionClass.assert_called_once_with(200)

    def test_returns_balance(self):
        self.assertEqual(self.account.current_balance(), 0)
    
    def test_printer_print_statement_called(self):
        self.account.print_statement()
        self.printer_mock.print_statement.assert_called_once_with()

    def test_print_statement_return(self):
        self.assertIsInstance(self.account.print_statement(), str)