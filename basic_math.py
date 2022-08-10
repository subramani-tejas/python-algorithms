####### is a number prime? #######
# def is_prime(number):
#     if (int(number) > 1):
#         for i in range(2, int(number)):
#             if(int(number) % i == 0):
#                 return True
#     else:
#         return False


# print("enter #: ")
# n = input()
# if(is_prime(n)):
#     print("Neither prime nor composite.")
# else:
#     print("Prime")
###################################


####### is it a leap year? #######
# def is_leap_year(year):
#     if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#         print("leap year.")
#         return
#     print("not a leap year")


# is_leap_year(2001)
###################################


####### multiplication table #######
# def multiplication_table_of(number):
#     for i in range(11):
#         print(number, "x", i, "=", number * i)


# multiplication_table_of(79)
###################################


####### HCF #######
# def find_hcf(num1, num2):
#     smaller_number = num1 if num1 < num2 else num2
#     for i in range(1, smaller_number+1):
#         if (num1 % i == 0 and num2 % i == 0):
#             hcf = i
#     return hcf


# print(find_hcf(54, 24))
###################################


####### HCF using euclidean algorithm #######
# def hcf_euclidean(x, y):
#     rem = x % y  # 6
#     while(rem):
#         x, y = y, rem
#         rem = x % y
#     return y


# print(hcf_euclidean(300, 400))
###################################
