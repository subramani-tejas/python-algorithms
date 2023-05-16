def even_or_odd() -> str:
    """ Write a program to print whether a number is even or odd.
        Take input from the user.
    """
    number = input("Enter a number: ")
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


def get_fibonacci_series(n):
    """To calculate Fibonacci Series up to n numbers.
    Sequence like 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
    """
    if n == 0:
        return [0]

    series = [0, 1]
    if n == 1:
        return series

    i = 2
    while i < n:
        a = series[i - 2]
        b = series[i - 1]
        series.append(a + b)
        i += 1

    return series


def is_palindrome(text):
    """Find out whether the given String is Palindrome or not."""
    n = len(text)
    i, j = 0, n - 1

    while i < j:
        if text[i] != text[j]:
            return False
        i += 1
        j -= 1

    return True


def is_armstrong_number(num):
    """ Find if number is Armstrong Number.
    An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the number \
    of digits in the number. Let's break it down with an example.
    Consider the number 153. It has three digits: 1, 5, and 3.
    We raise each digit to the power of 3 (since there are three digits in the number) and sum them up:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

    Another example. Consider the number 371. It has three digits: 3, 7, and 1.
    We raise each digit to the power of 3 and sum them up:
    3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
    """

    """Get number of digits and each digit in list."""
    number_of_digits = 0
    digits = []

    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        digits.append(digit)
        temp_num = temp_num // 10
        number_of_digits += 1

    digit_sum = 0
    for digit in digits:
        digit_sum += (digit ** number_of_digits)

    return num == digit_sum
