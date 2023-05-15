"""
TODO:
Take name as input and print a greeting message for that particular name.
Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.
Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)
Take 2 numbers as input and print the largest number.
Input currency in rupees and output in USD.
To calculate Fibonacci Series up to n numbers.
To find out whether the given String is Palindrome or not.
To find Armstrong Number between two given number.
"""


def even_or_odd() -> str:
    """ Write a program to print whether a number is even or odd.
        Take input from the user.
    """
    number = input("Enter a number: ")
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
