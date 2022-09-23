def selection_sort(arr):
    l = len(arr)
    for i in range(0, l):
        index_for_max = l - 1 - i
        max_num_index = find_max_index(arr, 0, index_for_max)
        swap(arr, max_num_index, index_for_max)
    return arr


def find_max_index(arr, start, end):
    max_num_index = start
    for i in range(start, end + 1):
        if arr[max_num_index] < arr[i]:
            max_num_index = i
    return max_num_index


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [4, 5, 1, 2, 3, 13, 6]
print(selection_sort(arr))
