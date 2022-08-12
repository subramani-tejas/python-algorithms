###### is a number prime? #######
def is_prime(number: int):
    flag = False
    if (number > 1):
        for i in range(2, number//2 + 1):
            if(number % i == 0):
                print("divisible by ", i)
                flag = False
                break
            else:
                flag = True
    else:
        return -1
    return flag


print("enter #: ")
n = int(input())
ans = is_prime(n)

if(ans == True):
    print("Prime")
elif (ans == False):
    print("Composite")
elif (ans == -1):
    print("Neither")
##################################


###### is it a leap year? #######
def is_leap_year(year):
    if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("leap year.")
        return
    print("not a leap year")


is_leap_year(2001)
##################################


###### multiplication table #######
def multiplication_table_of(number):
    for i in range(11):
        print(number, "x", i, "=", number * i)


multiplication_table_of(79)
##################################


###### HCF #######
def find_hcf(num1, num2):
    smaller_number = num1 if num1 < num2 else num2
    for i in range(1, smaller_number+1):
        if (num1 % i == 0 and num2 % i == 0):
            hcf = i
    return hcf


print(find_hcf(54, 24))
##################################


###### HCF using euclidean algorithm #######
def hcf_euclidean(x, y):
    rem = x % y  # 6
    while(rem):
        x, y = y, rem
        rem = x % y
    return y


print(hcf_euclidean(300, 400))
##################################


###### sum of user inputs #######
def sum_of_inputs():
    sum = 0
    while(1):
        number = input("Enter a number: ")
        if number == 'x':
            break
        sum += int(number)
    return sum


print(sum_of_inputs())
##################################


###### odd/even number #######
def is_odd_number(x):
    return True if int(x) % 2 != 0 else False


if(is_odd_number(input("Enter a number: "))):
    print("Odd")
else:
    print("Even")
##################################


###### fibonacci series upto n #######
def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


for i in range(10):
    print(fibo(i), end=" ")
##################################


###### is this text a palindrome? #######
def palindrome(text: str):
    # return text == text[::-1]
    j, flag = -1, True

    for character in text:
        if character != text[j]:
            flag = False
            break
        j -= 1

    return flag


if(palindrome("AsdA")):
    print("Palindrome")
else:
    print("Not Palindrome")
##################################


###### is this an armstrong number? #######
def armstrong_number(num: int):
    number_of_digits = len(str(num))
    temp = num
    sum = 0

    while(temp > 0):
        digit = temp % 10
        sum += digit ** number_of_digits
        temp //= 10

    return num == sum


print("153 ARMSTRONG") if(armstrong_number(153)) else print("REGULAR")
print("1634 ARMSTRONG") if(armstrong_number(1634)) else print("REGULAR")
print("15 ARMSTRONG") if(armstrong_number(15)) else print("REGULAR")
##################################


###### individual digits #######
def get_digits(num):
    unit_digit = num % 10
    tenth_digit = (num // 10) % 10
    hundredth_digit = (num // 100) % 10
    thousandth_digit = num // 1000
    print(thousandth_digit, hundredth_digit, tenth_digit, unit_digit)


get_digits(1513)
##################################


###### largest number in user inputs #######
def largest_number():
    largest = 0
    while(1):
        x = input("Enter a num: ")
        if x == 'x':
            break
        if int(x) > largest:
            largest = int(x)

    print("The largest number entered is: ", largest)


largest_number()
##################################


###### what is the case of the entered letter? #######
def case_check(letter):
    if len(letter) > 1:
        print("Invalid input")
    else:
        if 'a' <= letter <= 'z':
            print("lowercase")
        elif 'A' <= letter <= 'Z':
            print("UPPERCASE")


case_check(input("Enter a letter: "))
##################################


###### reverse a number #######
def reverse_number(x):
    print("Type of input: ", type(x))
    rev = 0

    # 21453
    # 21453 / 10 = 3, 5
    # rev = 3*10 + 5
    while(x > 0):
        rem = x % 10
        rev = rev * 10 + rem
        x = x // 10
    return rev


print(reverse_number(21453))
##################################


###### factorial #######
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)


print(factorial(13))
##################################


###### A Pythagorean triplet #######
# a ^ 2 + b ^ 2 = c ^ 2


def is_triplet(a, b, c):
    return "Pythagorean triplet" if a**2 + b**2 == c**2 else "Not triplet"


print(is_triplet(8, 15, 17))
##################################
