from typing import List


def missingNumber(nums: List[int]) -> int:
    arr = cyclic_sort(nums)
    for i in range(0, len(arr)):
        if i != arr[i]:
            return i
    return -1


def cyclic_sort(arr):
    i = 0

    while i < len(arr):
        correct_index = arr[i]
        if i == correct_index or correct_index >= len(arr):
            i += 1
        elif i != correct_index:
            swap(arr, i, correct_index)

    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [3, 0, 1]
print(missingNumber(nums=arr))
