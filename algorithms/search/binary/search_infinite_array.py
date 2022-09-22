# find position of element in infinite size array
# using regular array without calling its length method

# searching in chunks - starting from 1 and building up to N
def search_infinite_array(arr, key):
    start, end = 0, 1

    while key > arr[end]:
        temp = end + 1
        end = end + (end - start + 1) * 2
        start = temp

    return binary_search(arr, key, start, end)


def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + ((end - start) // 2)

        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


arr = [12, 13, 14, 17, 45, 46, 56, 67, 69, 79, 80, 83, 84, 88, 89, 91, 92, 112, 223, 321, 333, 334, 356, 364, 444, 545,
       5234, 6546, 6550, 6551, 6554, 6555, 6556, 6789]
key = 5234
res = search_infinite_array(arr, key)
print(res)
