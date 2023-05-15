from io import StringIO
from unittest.mock import patch
import unittest
import kk_assignments.src.week_002_initial_programs.main as source


class TestMain(unittest.TestCase):
    def test_even_or_odd(self):
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
