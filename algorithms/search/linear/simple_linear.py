from typing import Tuple


# works for strings and lists
def linear_search(arr, key) -> Tuple[int, int]:
    if len(arr) == 0:
        return -1, -1

    comparison_count = 0
    for i in range(0, len(arr)):
        comparison_count += 1
        if arr[i] == key:
            return i, comparison_count

    return -1, comparison_count


arr1 = "Hello"
key1 = "H"

res, comparisons = linear_search(arr=arr1, key=key1)


# print("target at index:", res)
# print("comparisons:", comparisons)


# searching in 2D arrays
def linear_2D_search(arr, key) -> Tuple[int, int]:
    number_of_rows = len(arr)
    for i in range(0, number_of_rows):
        number_of_columns = len(arr[i])
        for j in range(0, number_of_columns):
            if arr[i][j] == key:
                return i, j

    return -1, -1


arr_2d = [[1, 2, 3], [9, 8, 13, 12], [6, 7, 238]]
key_2d = 238
linear_2D_search(arr_2d, key_2d)
