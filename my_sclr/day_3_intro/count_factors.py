# Given an integer A, you need to find the count of it's factors.
# Factor of a number is the number which divides it perfectly leaving no remainder.
# Example : 1, 2, 3, 6 are factors of 6
import math


# O(N)
def count_factors_of(a):
    ans = 0
    n = math.floor(math.sqrt(a))
    for i in range(1, n + 1):
        if a % i == 0:
            ans = ans + 2
        if i * i == a:
            ans = ans - 1
    return ans


# returns factors list
def get_factors(n):
    factors = []
    n = math.floor(math.sqrt(n))
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(math.floor(n / i))

    return factors
