"""
Permutations refer to the different ways we can arrange a certain number of objects
from the set, taking into account the order or sequence of selection. It focuses on
both the selection and arrangement of objects. The order in which the objects are selected matters.

If we want to arrange two objects from this set, considering the order, the possible
permutations would be: AB, AC, BA, BC, CA, and CB. Here, the order of selection matters,
so AB is different from BA.

nPr (permutation), on the other hand, represents the number of ways to arrange r items
from a set of n items, considering the order of selection.

The formula for nPr is:
    nPr = n! / (n-r)!
"""

from kk_assignments.src.week_003_conditionals_loops.factorial import get_factorial


def get_npr(n, r):
    """ O(n) """
    n_factorial = get_factorial(n)
    nr_factorial = get_factorial(n - r)

    return n_factorial // nr_factorial
