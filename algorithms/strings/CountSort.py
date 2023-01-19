TOTAL_ALPHABETS = 26


def count_sort_characters(arr):
    count = [0] * TOTAL_ALPHABETS
    res = []

    # frequency character array
    for item in arr:
        count[ord(item) - ord('a')] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            res.append(chr(i + ord('a')))

    return res


def count_sort_numbers(arr):
    max_size = max(arr)
    count = [0] * (max_size + 1)
    res = []

    # count array
    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            res.append(i)

    return res


chr_arr = ['b', 'z', 'd', 'a', 'd', 'a', 'c', 'd']
int_arr = [6, 3, 3, 6, 7, 8, 7, 3, 7]

print(count_sort_characters(chr_arr))
print(count_sort_numbers(int_arr))
