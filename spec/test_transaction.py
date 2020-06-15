from unittest import TestCase
from src.transaction import Transaction

class TestTransaction(TestCase):
    
    def test_records_transaction_value(self):
        transaction = Transaction(200)
        self.assertEqual(transaction.value, 200)