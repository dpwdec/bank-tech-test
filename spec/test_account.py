import unittest
from src.account import Account

class TestAccount(unittest.TestCase):

    def test_returns_balance(self):
        account = Account(0)
        self.assertEqual(account.current_balance(), 0)