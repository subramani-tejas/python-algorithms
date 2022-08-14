from sys import getsizeof

values_gen = (x*2 for x in range(5000))

# generator object
print(type(values_gen))


# generator used in case of large data set
# every iteration spits out a new value
# doesn't store everything in memory
# is iterable
# lesser size gen object
# has no len

values_list = [x*2 for x in range(5000)]
values_set = {x*2 for x in range(5000)}

print("list:", getsizeof(values_list))
print("set:", getsizeof(values_set))
print("gen:", getsizeof(values_gen))

print("###############################")

# unpacking operator *
list_ex = [*range(4), *"tjs"]
print(list_ex)

dict_ex1 = {"x": 12}
dict_ex2 = {"x": 23, "y": 19}
combined_dict = {**dict_ex1, **dict_ex2, "z": 63}
print(combined_dict)
