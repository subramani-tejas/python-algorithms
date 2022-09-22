# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def num_of_even_digits_in(numbers_):
    count = 0
    for item in numbers_:
        if is_even_digits(item):
            count += 1
    return count


def is_even_digits(num):
    digits = 0
    while num > 0:
        num = num // 10
        digits += 1

    return digits % 2 == 0


numbers = [18, 191, 5422, 12]
res = num_of_even_digits_in(numbers)
print(res)
