# print items in a matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        print("row: ", matrix[i])
        for j in range(len(matrix[i])):
            print("element: ", matrix[i][j])


sample = [[1, 2], [3, 4]]
print_matrix(sample)


# make a list
numbers = list(range(10, 21))

# reverse the list
print("reversed: ", numbers[::-1])

first, *others, second_to_last, last = numbers
print("first: ", first)
print("second to last: ", second_to_last)
print("last: ", last)
print("others: ", others)


letters = list("TEJAS")
for index, letter in enumerate(letters):
    print(index, letter)

for i in range(len(letters)):
    if 'J' in letters:
        letters.remove('J')
print(letters)


comics = [
    ("Doomsday Clock", 2),
    ("Watchmen", 1),
    ("Before Watchmen", 0)
]


def sort_comic(comic):
    return comic[1]


comics.sort(key=sort_comic, reverse=True)

# using lambda expression
# ... key=lambda func_params: return_expression

comics.sort(key=lambda comic: comic[1])
sorted(comics, key=lambda x: x[1], reverse=True)
print(comics)


# map function to get the numbers only as list
mapped_comics = list(map(lambda comic: comic[1], comics))
print("mapped_comics: ", mapped_comics)

# map using list comprehension
# [<return_expr> for item in items <condition>]
comprehension_mapped_comics = [comic[1] for comic in comics]
print("comprehension_mapped_comics: ", comprehension_mapped_comics)

# filter function - passing a condition
filtered_comics = list(filter(lambda comic: comic[1] != 0, comics))
print("filtered_comics: ", filtered_comics)

# filter using list comprehension
comprehension_filtered_comics = [comic for comic in comics if comic[1] != 0]
print("comprehension_filtered_comics: ", comprehension_filtered_comics)


# zip - to deal with multiple functions
# [('t', 1, 4), ('j', 2, 5), ('s', 3, 6)]
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list(zip("tjs", list1, list2)))
