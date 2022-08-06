# set1 = {1, 2, 3, 1, 2, 4, 5, 3, 4, 8, 9, 7, 10}
# for i in range(len(set1)):
#     print(i, end=" ")


# def find_sum(a, b):
#     try:
#         print(a+c)
#     except ValueError:
#         print("Function name error")
#     finally:
#         print("Sum finally")


# try:
#     find_sum(12, 13)
# except NameError:
#     print("Invocation name error")
# finally:
#     print("Invocation finally")

def sample(value):
    sum1 = 0
    for i in value:
        if i % 2 != 0:
            sum1 += value[i]
        else:
            sum1 -= i
    print(sum1)


dict1 = {1: 2, 2: 4, 3: 6, 5: 8}
sample(dict1)
