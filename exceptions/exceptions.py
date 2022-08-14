
try:
    # file = open("exceptions.py")
    age = int(input("enter age: "))
    print("try done")
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("invalid entry...")
    print(ex, type(ex))
else:
    print("valid entry...")
finally:
    # file.close()
    print("finally exection")

print("continue")


# # raising exceptions

def calc_xfactor(age: int):
    if age <= 0:
        raise ArithmeticError("age can't be 0")
    return 100 / age


try:
    print(calc_xfactor(int(input("enter age: "))))
except ArithmeticError as ex:
    print(ex)
