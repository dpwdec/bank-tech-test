from unittest import TestCase
from datetime import datetime
from src.account import Account
from src.transaction import Transaction
from src.printer import Printer

class TestAccountIntegration(TestCase):

    def test_user_can_print_account_statement(self):
        """
        Integration statement output
        date       || credit  || debit   || balance
        14/01/2012 ||         || 200.00  || 0.00   
        20/02/2015 || 50.55   ||         || 200.00 
        21/02/2012 ||         || 3000.00 || 149.45 
        01/03/2015 || 3.50    ||         || 3149.45
        11/01/2016 || 10.20   ||         || 3145.95
        """

        printer = Printer()
        account = Account(Transaction, printer)

        account.deposit(200)
        account.withdraw(50.55)
        account.deposit(3000)
        account.withdraw(3.5)
        account.withdraw(10.20)

        statement = ("date       || credit  || debit   || balance"
        "\n" + datetime.now().strftime("%d/%m/%Y") + " ||         || 200.00  || 0.00   "
        "\n" + datetime.now().strftime("%d/%m/%Y") + " || 50.55   ||         || 200.00 "
        "\n" + datetime.now().strftime("%d/%m/%Y") + " ||         || 3000.00 || 149.45 "
        "\n" + datetime.now().strftime("%d/%m/%Y") + " || 3.50    ||         || 3149.45"
        "\n" + datetime.now().strftime("%d/%m/%Y") + " || 10.20   ||         || 3145.95")

        self.assertEqual(account.print_statement(), statement)
        

