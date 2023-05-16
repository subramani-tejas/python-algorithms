from unittest.mock import patch
import unittest
import kk_assignments.src.week_002_initial_programs.main as source


class TestMain(unittest.TestCase):
    def test_even_or_odd(self):
        try:
            # Test case 1: Even number
            even_num = 4
            with patch('builtins.input', return_value=even_num):
                assert source.even_or_odd() == "even"

            # Test case 2: Odd number
            odd_num = 7
            with patch('builtins.input', return_value=odd_num):
                assert source.even_or_odd() == "odd"

            # Test case 3: Zero
            zero = 0
            with patch('builtins.input', return_value=zero):
                assert source.even_or_odd() == "even"

            print("even_or_odd PASSED OK")

        except AssertionError:
            print("even_or_odd FAILED")

    def test_get_fibonacci_series(self):
        try:
            expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]
            self.assertEqual(source.get_fibonacci_series(9), expected)

            expected_zero = [0]
            self.assertEqual(source.get_fibonacci_series(0), expected_zero)

            print("get_fibonacci_series PASSED OK")
        except AssertionError:
            print("get_fibonacci_series FAILED")

    def test_is_palindrome(self):
        try:
            self.assertTrue(source.is_palindrome("malayalam"))
            self.assertFalse(source.is_palindrome("car"))
            print("is_palindrome PASSED OK")
        except AssertionError:
            print("is_palindrome FAILED")

    def test_is_armstrong_number(self):
        try:
            self.assertTrue(source.is_armstrong_number(8208))
            print("is_armstrong_number PASSED OK")
        except AssertionError:
            print("is_armstrong_number FAILED")
