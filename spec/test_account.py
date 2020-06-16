from unittest import TestCase
from unittest import mock
from src.account import Account

class TestAccount(TestCase):
    
    def setUp(self):
        # set up mock Transaction class and object
        transaction_object = mock.Mock()
        self.TransactionClass = mock.Mock()
        self.TransactionClass.return_value = transaction_object
        # setup mock printer
        self.printer_mock = mock.Mock()
        self.printer_mock.print_statement.return_value = ""
        # instantiate account test object
        self.account = Account(self.TransactionClass, self.printer_mock)

class TestTransactions(TestAccount):

    def test_responds_to_transactions(self):
        self.assertTrue(hasattr(self.account, 'transactions'))

    def test_has_empty_list_of_transactions(self):
        """
        Account is initialized with a list an empty
        transactions list.
        """
        self.assertEqual(self.account.transactions, [])

class TestTransact(TestAccount):

    def test_transact_calls_transaction_class(self):
        """
        Calling transact calls Transaction to create a
        new instance of Transaction
        """
        self.account.transact(200)
        self.TransactionClass.assert_called_once_with(200)

    def test_single_transact(self):
        """
        Calling transact pushes a new instance of a transaction
        object onto the Account object's transaction array
        """
        self.account.transact(200)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertIsInstance(self.account.transactions[0], mock.Mock)

    def test_multiple_transact(self):
        """
        Calling transact multiple times pushes a new instances 
        of the transaction object onto the Account object's transaction array
        """
        self.account.transact(200)
        self.account.transact(-200)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertIsInstance(self.account.transactions[0], mock.Mock)
        self.assertIsInstance(self.account.transactions[1], mock.Mock)

class TestAccountTests(TestAccount):
    
    
    def test_printer_print_statement_called(self):
        self.account.print_statement()
        self.printer_mock.print_statement.assert_called_once_with([])

    def test_print_statement_return(self):
        self.assertIsInstance(self.account.print_statement(), str)