"""
Find the factorial of a number.
0! = 1! = 1
n! = n . (n-1)!
"""


def get_factorial(n):
    """
    Time Complexity: O(n)
    :param n: number
    :return: factorial of n (n!)
    """
    if n == 0 or n == 1:
        return 1

    i = 2
    factorial = 1

    while i <= n:
        factorial *= i
        i += 1

    return factorial
