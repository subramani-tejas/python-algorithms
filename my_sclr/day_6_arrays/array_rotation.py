import reverse_array


# rotate array k times
def rotate_by(arr, k):
    # reverse full array
    i, j = 0, len(arr) - 1
    reverse_array.reverse_in_range(arr, i, j)

    # reverse 0 -> k-1
    k = k % len(arr)
    reverse_array.reverse_in_range(arr, 0, k - 1)

    # reverse k -> n-1
    reverse_array.reverse_in_range(arr, k, len(arr) - 1)

    return arr


arr = [4, 5, 12, 432, 2, 90]
# print(rotate_by(arr, 3))
