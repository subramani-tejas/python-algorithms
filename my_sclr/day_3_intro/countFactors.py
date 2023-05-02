# Given an integer A, you need to find the count of it's factors.
# Factor of a number is the number which divides it perfectly leaving no remainder.
# Example : 1, 2, 3, 6 are factors of 6
import math


# O(N)
def countFactorsOf(self, A):
    ans = 0
    n = math.floor(math.sqrt(A))
    for i in range(1, n + 1):
        if A % i == 0:
            ans = ans + 2
        if i * i == A:
            ans = ans - 1
    return ans


# returns factors list
def get_factors(N):
    factors = []
    n = math.floor(math.sqrt(N))
    for i in range(1, n + 1):
        if N % i == 0:
            factors.append(i)
            if i * i != N:
                factors.append(math.floor(N / i))

    return factors
