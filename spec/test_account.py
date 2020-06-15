import unittest
from src.account import Account

class TestAccount(unittest.TestCase):

    def test_returns_balance(self):
        account = Account(0)
        self.assertEqual(account.current_balance(), 0)

    def test_has_list_of_transactions(self):
        account = Account(0)
        self.assertEqual(account.transactions, [])

    def test_execute_single_transaction(self):
        account = Account(0)
        account.transact(200)
        self.assertEqual(account.transactions[0], 200)
    
    def test_execute_multiple_transactions(self):
        account = Account(0)
        account.transact(200)
        account.transact(-50)
        self.assertEqual(len(account.transactions), 2)