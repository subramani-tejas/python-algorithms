def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def cyclic_sort(arr):
    i = 0

    while i < len(arr):
        correct_index = arr[i] - 1
        if i != correct_index:
            swap(arr, i, correct_index)
        else:
            i += 1

    return arr


arr = [3, 5, 2, 1, 4]
print(cyclic_sort(arr))
