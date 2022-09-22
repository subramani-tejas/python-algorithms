# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
import math


def num_of_even_digits_in(numbers_):
    count = 0
    for item in numbers_:
        if is_even_digits_optimized(item):
            count += 1
    return count


def is_even_digits(num):
    digits = 0
    while num > 0:
        num = num // 10
        digits += 1

    return digits % 2 == 0


# even digits optimized using log10(num)
def is_even_digits_optimized(num):
    digits = int(math.log10(num)) + 1
    return digits % 2 == 0


numbers = []
res = num_of_even_digits_in(numbers)
print(res)
