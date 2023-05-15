def get_multiplication_table(num):
    """
    :param num: integer
    :return: Take a number as input and print the multiplication table for it.
    """

    res = []
    for i in range(1, 11):
        # print(f"{num} x {i} = {num * i}")
        res.append(num * i)
    return res


def is_leap_year(year):
    """
    :param year: any year after 1582
    :return: Input a year and find whether it is a leap year or not.
    """
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


def get_HCF(x: int, y: int) -> int:
    """
    :param x: integer
    :param y: integer
    :return: Finds HCF (GCD).This function uses factors method.
    It's the largest +number that divides both numbers without remainder.

    Example using factors:
    HCF (24, 36) = 12
    24 factors: [1, 2, 3, 4, 6, 8, 12, 24]
    36 factors: [1, 2, 3, 4, 6, 9, 12, 18, 36]
    The largest number common to both factors is 12.

    Example using prime factorization:
    HCF (24, 36) = 12
    24 prime factorization: 2 x 2 x 2 x 3
    36 prime factorization: 2 x 2 x 3 x 3
    Common factors from both, 2 x 2 x 3 = 12

    TC/SC: O(X + Y)
    """

    if x == 0 and y == 0:
        print("undefined")
        return -1

    if x == 0:
        print(y)
        return y

    if y == 0:
        print(x)
        return x

    # O(X) + O(Y)
    x_factors, y_factors = get_factors(x), get_factors(y)
    x_factors_len, y_factors_len = len(x_factors), len(y_factors)
    i, j = 0, 0
    common_factors = []

    while i < x_factors_len and j < y_factors_len:
        if x_factors[i] == y_factors[j]:
            common_factors.append(x_factors[i])
            i += 1
            j += 1
        elif x_factors[i] < y_factors[j]:
            i += 1
        else:
            j += 1

    print(common_factors[len(common_factors) - 1])
    return common_factors[len(common_factors) - 1]


def get_factors(n: int) -> list:
    """
    :return: returns all factors of a number
    for ex. 24: [1, 2, 3, 4, 6, 8, 12, 24]
    TC/SC: O(N)
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    print(f"{n} factors: {factors}")
    return factors


def get_prime_factorization(n: int) -> list:
    """
    :param n: number
    :return: prime factorization of the number

    for ex. 24: 2 x 2 x 2 x 3

    O(log N)
    """
    temp = n
    prime_factors = []

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                prime_factors.append(i)
                break

    print(f"prime factors of {temp}: {prime_factors}")
    return prime_factors


def get_LCM(x, y):
    """
    :param x, y: integers
    :return: return least common multiple (LCM) of two numbers.

    Example, LCM (24, 36) = 72
    Multiples of 24: 24, 48, 72, 96, 120, 144 ...
    Multiples of 36: 36, 72, 108, 144 ...
    Least common of the multiples is 72

    Example using prime factorization,
    24 prime factorization: 2 x 2 x 2 x 3
    36 prime factorization: 2 x 2 x 3 x 3
    Common factors from both are 2 & 3
    2^3 (2's max power raised is 3)
    3^2 (3's max power raised is 2)
    LCM = 2^3 x 3^2 = 8 x 9 = 72

    LCM(0, 0) = undefined
    LCM(0, N) = 0
    """
    x_factors = get_prime_factorization(x)
    y_factors = get_prime_factorization(y)

    lcm_factors = []
    lcm = 1
    i, j = 0, 0

    while i < len(x_factors) and j < len(y_factors):
        if x_factors[i] == y_factors[j]:
            lcm_factors.append(x_factors[i])
            i += 1
            j += 1
        elif x_factors[i] > y_factors[j]:
            lcm_factors.append(y_factors[j])
            j += 1
        else:
            # x_factors[i] < y_factors[j]:
            lcm_factors.append(x_factors[i])
            i += 1

    # add any leftover items to lcm factors
    while i < len(x_factors):
        lcm_factors.append(x_factors[i])
        i += 1

    while j < len(y_factors):
        lcm_factors.append(y_factors[j])
        j += 1

    for factor in lcm_factors:
        lcm = lcm * factor

    print(f"LCM factors are: {lcm_factors}")
    print(f"LCM: {lcm}")
    return lcm


def get_frequency_map(arr: list) -> dict:
    """
    :param arr: input array
    :return: dictionary containing frequency of items in array
    """
    freq_map = {}
    for item in arr:
        if item not in freq_map:
            freq_map[item] = 1
        else:
            freq_map[item] += 1

    print(f"frequency map of {arr}: {freq_map}")
    return freq_map


def print_sum_of_inputs():
    """
    :return: Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
    """
    sum = 0
    while True:
        input_text = input("Enter number. Enter x when done.")
        if input_text == 'x':
            break
        sum += int(input_text)

    print(sum)
    return sum
