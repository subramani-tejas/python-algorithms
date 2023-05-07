# Take a number as input and print the multiplication table for it.
def get_multiplication_table(num):
    res = []
    for i in range(1, 11):
        # print(f"{num} x {i} = {num * i}")
        res.append(num * i)
    return res


# Input a year and find whether it is a leap year or not.
def is_leap_year(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


# Take 2 numbers as inputs and find their HCF.
def find_HCF(x, y):
    pass


# Take 2 numbers as inputs and find their LCM.
def find_LCM(x, y):
    pass


# Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
def print_sum_of_inputs():
    pass
