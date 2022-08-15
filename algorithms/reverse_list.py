# reverse a list using 2 pointers

def reverse(list):
    start, end = 0, len(sample) - 1

    while (start < end):
        swap(list, start, end)
        start += 1
        end -= 1


def swap(list, x, y):
    list[x], list[y] = list[y], list[x]
    return list


sample = [1, 2, 3, 4, 5, 6]
reverse(sample)
print("reversed: ", sample)


# optimized version
sample2 = [1, 2, 3, 4, 5, 6, 7]
print("reversed: ", sample2[::-1])
