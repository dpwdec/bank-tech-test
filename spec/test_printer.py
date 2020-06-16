from unittest import TestCase
from src.printer import Printer

class TestPrinter(TestCase):

    def test_has_print_statement_method(self):
        printer = Printer()
        self.assertTrue(hasattr(printer, 'print_statement'))