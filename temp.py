numbers = list(range(10, 21))

# reverse the list
# print(numbers[::-1])

first, *others, second_to_last = numbers
# print(first, second_to_last)
# print(others)

letters = ['a', 'b', 'c', 'b', 'b', 'b', 'x']
# for index, letter in enumerate(letters):
#     print(index, letter)

# for i in range(len(letters)):
#     if 'b' in letters:
#         letters.remove('b')
# print(letters)

comics = [
    ("Doomsday Clock", 2),
    ("Watchmen", 1),
    ("Before Watchmen", 0)
]


# def sort_comic(comic):
#     return comic[1]


# comics.sort(key=sort_comic, reverse=True)
comics.sort(key=lambda comic: comic[1])
print(comics)
