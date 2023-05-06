import io
import sys
import unittest
import kk_assignments.src.flow_of_program_01.main as main_module


class TestMain(unittest.TestCase):

    def test_get_multiplication_table(self):
        num = 5
        expected_output = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        main = main_module.Main()
        captured_output = main.get_multiplication_table(num)
        assert captured_output == expected_output
        print("test_print_multiplication_table passed OK")
