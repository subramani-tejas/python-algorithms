# You are given an integer A. You have to tell whether it is a perfect number or not.
# Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
# A proper divisor of a natural number is the divisor that is strictly less than the number.
import my_sclr.day_3_intro.count_factors as callFactors


def findPerfectNumber(N):
    # N=6
    # [1, 6, 2, 3]
    factors = callFactors.get_factors(N)

    # [1, 2, 3]
    proper_factors = []
    for factor in factors:
        if factor < N:
            proper_factors.append(factor)

    sum = 0
    for factor in proper_factors:
        sum += factor

    if sum == N:
        return 1
    else:
        return 0
