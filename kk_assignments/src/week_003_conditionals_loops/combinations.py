"""
Combinations refer to the different ways we can select a certain number of
objects from the set, without considering the order of selection.

If we want to choose two objects from this set without considering the order,
the possible combinations would be: AB, AC, and BC. The order of selection
does not matter, so AB is the same as BA.

nCr (combination) represents the number of ways to choose r items from a
set of n items without considering the order of selection.

The formula for nCr is:
    nCr = n! / (r!(n-r)!)
"""

from kk_assignments.src.week_003_conditionals_loops.factorial import get_factorial


def get_ncr(n, r):
    """ O(n) """
    n_factorial = get_factorial(n)
    r_factorial = get_factorial(r)
    nr_factorial = get_factorial(n - r)

    return n_factorial // (r_factorial * nr_factorial)
