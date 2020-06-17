from unittest import TestCase
from unittest import mock
from src.printer import Printer

class TestPrinter(TestCase):

    def setUp(self):
        self.printer = Printer()
        # set up positive transaction mock
        self.positive_transaction = mock.Mock()
        self.positive_transaction.get_formatted_date.return_value = "14/01/2012"
        self.positive_transaction.is_debit.return_value = True
        self.positive_transaction.value = 200
        # set up negative transaction mock
        self.negative_transaction = mock.Mock()
        self.negative_transaction.get_formatted_date.return_value = "20/02/2015"
        self.negative_transaction.is_debit.return_value = False
        self.negative_transaction.value = -50

    def test_respond_to_print_statement_method(self):
        printer = Printer()
        self.assertTrue(hasattr(printer, 'print_statement'))

class TestIntegerPrinter(TestPrinter):

    def test_print_zero_line_statement(self):
        """
        If print statement is pass an empty array 
        it will print only account headers:
        date       || credit  || debit  || balance
        """
        printer = Printer()
        self.assertEqual(printer.print_statement([]), "date       || credit  || debit   || balance")
    
    def test_print_debit_one_line_statement(self):
        """
        If transactions is contains one transaction for 200:
        date       || credit  || debit   || balance
        14/01/2012 ||         || 200.00  || 0.00   
        """
        statement =  "date       || credit  || debit   || balance\n14/01/2012 ||         || 200.00  || 0.00   "
        self.assertEqual(self.printer.print_statement([self.positive_transaction]), statement)
    
    def test_print_credit_one_line_statement(self):
        """
        If transactions is contains one transaction for -50:
        date       || credit  || debit   || balance
        14/01/2012 ||         || 200.00  || 0.00   
        """
        statement = "date       || credit  || debit   || balance\n20/02/2015 || 50.00   ||         || 0.00   "
        self.assertEqual(self.printer.print_statement([self.negative_transaction]), statement)
    
    def test_print_multi_line_statement(self):
        """
        If transactions is two transactions for 200 and -50:
        date       || credit  || debit   || balance
        14/01/2012 ||         || 200.00  || 0.00   
        20/02/2015 || 50.00   ||         || 200.00 
        """
        statement = "date       || credit  || debit   || balance\n14/01/2012 ||         || 200.00  || 0.00   \n20/02/2015 || 50.00   ||         || 200.00 "
        self.assertEqual(self.printer.print_statement([self.positive_transaction, self.negative_transaction]), statement)
    
class TestFloatPrinter(TestCase):

    def setUp(self):
        self.printer = Printer()
        # set up positive transaction mock
        self.positive_transaction = mock.Mock()
        self.positive_transaction.get_formatted_date.return_value = "14/01/2012"
        self.positive_transaction.is_debit.return_value = True
        self.positive_transaction.value = 200.20
        # set up negative transaction mock
        self.negative_transaction = mock.Mock()
        self.negative_transaction.get_formatted_date.return_value = "20/02/2015"
        self.negative_transaction.is_debit.return_value = False
        self.negative_transaction.value = -50.55

    def test_print_debit_one_line_statement(self):
        """
        If transactions is contains one transaction for 200.20:
        date       || credit  || debit   || balance
        14/01/2012 ||         || 200.20  || 0.00   
        """
        statement =  "date       || credit  || debit   || balance\n14/01/2012 ||         || 200.20  || 0.00   "
        self.assertEqual(self.printer.print_statement([self.positive_transaction]), statement)

    def test_print_multi_line_statement(self):
        """
        If transactions is two transactions for 200.20 and -50.55:
        date       || credit  || debit   || balance
        14/01/2012 ||         || 200.22  || 0.00   
        20/02/2015 || 50.55   ||         || 200.22 
        """
        statement = "date       || credit  || debit   || balance\n14/01/2012 ||         || 200.20  || 0.00   \n20/02/2015 || 50.55   ||         || 200.20 "
        self.assertEqual(self.printer.print_statement([self.positive_transaction, self.negative_transaction]), statement)