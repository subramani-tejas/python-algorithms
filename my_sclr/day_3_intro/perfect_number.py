# You are given an integer A. You have to tell whether it is a perfect number or not.
# Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
# A proper divisor of a natural number is the divisor that is strictly less than the number.
import my_sclr.day_3_intro.count_factors as call_factors


def findPerfectNumber(n):
    # N=6
    # [1, 6, 2, 3]
    factors = call_factors.get_factors(n)

    # [1, 2, 3]
    proper_factors = []
    for factor in factors:
        if factor < n:
            proper_factors.append(factor)

    my_sum = 0
    for factor in proper_factors:
        my_sum += factor

    if my_sum == n:
        return 1
    else:
        return 0
