numbers = [1, 2, 3, 4, 5]
first_set = set(numbers)
second_set = {1, 2, 5, 6}

# # 1   2   3   4   5
# # 1   2           5   6

print("union: ", first_set | second_set)
print("intersection: ", first_set & second_set)

print("a - b: ", first_set - second_set)
print("b - a: ", second_set - first_set)

print("combo of items present in either but not both: ", first_set ^ second_set)

print("yes") if 22 in (first_set and second_set) else print("no")
