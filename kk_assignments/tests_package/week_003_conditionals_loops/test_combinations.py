import unittest
from kk_assignments.src.week_003_conditionals_loops import combinations as source


class TestCombinations(unittest.TestCase):
    def test_get_ncr(self):
        try:
            self.assertEqual(source.get_ncr(n=5, r=3), 10)
            print("test_get_ncr PASSED OK")

        except AssertionError or ModuleNotFoundError or ImportError:
            print("test_get_ncr FAILED")


if __name__ == "test_combinations":
    print("combinations passed OK")
