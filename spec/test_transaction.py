from unittest import TestCase
from unittest import mock
from src.transaction import Transaction

class TestTransaction(TestCase):
    
    def test_records_transaction_value(self):
        date_object = mock.Mock()
        transaction = Transaction(200, date_object)
        self.assertEqual(transaction.value, 200)
    
    def test_records_transaction_date(self):
        date_object = mock.Mock()
        transaction = Transaction(200, date_object)
        self.assertEqual(transaction.date, date_object)

    def test_get_formatted_date(self):
        date_object = mock.Mock()
        transaction = Transaction(200, date_object)
        transaction.get_formatted_date()
        transaction.date.strftime.assert_called_with("%d/%m/%Y")