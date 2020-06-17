from unittest import TestCase
from unittest import mock
from src.transaction import Transaction

class TestTransaction(TestCase):
    
    def setUp(self):
        self.date_object = mock.Mock()
        self.transaction = Transaction(200, self.date_object)

class TestTransactionValue(TestTransaction):

    def test_records_transaction_value(self):
        self.assertEqual(self.transaction.value, 200)

class TestTransactionDate(TestTransaction):
    
    def test_records_transaction_date(self):
        self.assertEqual(self.transaction.date, self.date_object)

class TestTransactionType(TestTransaction):

    def test_is_debit_true(self):
        self.assertTrue(self.transaction.is_debit())
    
    def test_is_debite_false(self):
        self.transaction = Transaction(-200, self.date_object)
        self.assertFalse(self.transaction.is_debit())