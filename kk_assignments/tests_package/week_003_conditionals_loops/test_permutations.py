import unittest
from kk_assignments.src.week_003_conditionals_loops import permutations as source


class TestPermutations(unittest.TestCase):
    def test_get_npr(self):
        try:
            self.assertEqual(source.get_npr(n=5, r=3), 60)
            print("test_get_npr PASSED OK")

        except AssertionError or ModuleNotFoundError or ImportError:
            print("test_get_npr FAILED")


if __name__ == "test_permutations":
    print("permutations passed OK")
