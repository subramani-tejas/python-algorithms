import io
import sys
import unittest
import kk_assignments.src.flow_of_program_01.main as source


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
