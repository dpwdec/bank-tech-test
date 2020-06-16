from unittest import TestCase
from unittest import mock
from src.printer import Printer

class TestPrinter(TestCase):

    def test_has_print_statement_method(self):
        printer = Printer()
        self.assertTrue(hasattr(printer, 'print_statement'))

    def _print_zero_line_statement(self):
        """
        If print statement is pass an empty array 
        it will print only account headers:
        date       || credit  || debit  || balance
        """
        printer = Printer()
        self.assertEqual(printer.print_statement([]), "date       || credit  || debit   || balance")
    
    def test_print_one_line_statement(self):
        """
        If transactions is contains one transaction for 200:
        date       || credit  || debit   || balance
        14/01/2012 ||         || 200.00  || 0.00   
        """
        statement =  "date       || credit  || debit   || balance\n14/01/2012 ||         || 200.00  || 0.00   "
        positive_transaction = mock.Mock()
        positive_transaction.get_formatted_date.return_value = "14/01/2012"
        positive_transaction.is_debit.return_value = True
        positive_transaction.value = 200
        printer = Printer()
        self.assertEqual(printer.print_statement([positive_transaction]), statement)