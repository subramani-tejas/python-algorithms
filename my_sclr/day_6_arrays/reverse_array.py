# reverse full array
# O(N)
def reverse(self, arr):
    x = len(arr) - 1
    reverse_array = []
    while x >= 0:
        reverse_array.append(arr[x])
        x = x - 1
    return reverse_array


# reverse array in range
# O(j-i)
def reverse_in_range(arr, i, j):
    while i < j:
        swap(arr, i, j)
        i = i + 1
        j = j - 1
    return arr


# O(1)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr
