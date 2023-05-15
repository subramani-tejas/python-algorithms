from io import StringIO
from unittest.mock import patch
import unittest
import kk_assignments.src.week_001_flow_of_program.main as source


class TestMain(unittest.TestCase):

    def test_get_multiplication_table(self):
        num = 5
        expected_output = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        captured_output = source.get_multiplication_table(num)
        assert captured_output == expected_output
        print("print_multiplication_table() passed OK")

    def test_is_leap_year(self):
        assert source.is_leap_year(1900) == False
        assert source.is_leap_year(2000) == True
        assert source.is_leap_year(2020) == True
        print("is_leap_year() passed OK")

    def test_get_HCF(self):
        self.assertEqual(source.get_HCF(24, 36), 12)
        self.assertEqual(source.get_HCF(10, 0), 10)
        print("get_HCF() passed OK")

    def test_get_LCM(self):
        self.assertEqual(source.get_LCM(24, 36), 72)
        self.assertEqual(source.get_LCM(10, 0), 10)
        print("get_LCM() passed OK")

    def test_print_sum_of_inputs(self):
        @patch('sys.stdout', new_callable=StringIO)
        @patch('builtins.input', side_effect=['1', '2', '3', 'x'])
        def test_sum_numbers(self, mock_input, mock_output):
            self.assertEqual(source.print_sum_of_inputs(), 6)
            self.assertEqual(mock_output.getvalue(),
                             "Enter number. Enter x when done. "
                             "Enter number. Enter x when done. "
                             "Enter number. Enter x when done. "
                             "Enter number. Enter x when done. ")
