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

class TestDeposit(TestAccount):
    
    def test_deposit_calls_transaction_class(self):
        """
        Calling deposit calls Transaction to create a
        new instance of Transaction
        """
        self.account.deposit(200)
        self.TransactionClass.assert_called_once_with(200)

    def test_deposit_converts_negative_amounts(self):
        """
        Calling deposit with a negative amount
        converts the amount to a positive amount
        """
        self.account.deposit(-200)
        self.TransactionClass.assert_called_once_with(200)

    def test_deposit_adds_to_transactions(self):
        """
        Calling deposit pushes a new instance of a transaction
        object onto the Account object's transaction array
        """
        self.account.deposit(200)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertIsInstance(self.account.transactions[0], mock.Mock)


class TestWithdraw(TestAccount):

    def test_withdraw_calls_transaction_class(self):
        """
        Calling withdraw calls Transaction to create a
        new instance of Transaction with negative amount
        """
        self.account.withdraw(200)
        self.TransactionClass.assert_called_once_with(-200)

    def test_withdraw_adds_to_transactions(self):
        """
        Calling withdraw pushes a new instance of a transaction
        object onto the Account object's transaction array
        """
        self.account.withdraw(200)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertIsInstance(self.account.transactions[0], mock.Mock)

class TestTransactions(TestAccount):

    def test_multiple_transactions(self):
        """
        Calling transact multiple times pushes a new instances 
        of the transaction object onto the Account object's transaction array
        """
        self.account.deposit(200)
        self.account.withdraw(200)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertIsInstance(self.account.transactions[0], mock.Mock)
        self.assertIsInstance(self.account.transactions[1], mock.Mock)

class TestPrintStatement(TestAccount):
    
    def test_printer_print_statement_called(self):
        self.account.print_statement()
        self.printer_mock.print_statement.assert_called_once_with([])

    def test_print_statement_return(self):
        self.assertIsInstance(self.account.print_statement(), str)