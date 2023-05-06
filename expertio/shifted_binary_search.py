def shiftedBinarySearch(arr, key):
    pivot_index = find_pivot_index(arr)

    # if no pivot - regular bin search
    if pivot_index == -1:
        return binary_search(arr, key, 0, len(arr) - 1)

    # if key is pivot element
    if arr[pivot_index] == key:
        return pivot_index

    search_left = binary_search(arr, key, 0, pivot_index - 1)
    if search_left == -1:
        return binary_search(arr, key, pivot_index + 1, len(arr) - 1)
    else:
        return search_left


def find_pivot_index(arr):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        if mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1
        if arr[mid] <= arr[start]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1
