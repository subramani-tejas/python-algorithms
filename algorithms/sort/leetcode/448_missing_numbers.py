from typing import List


def missingNumber(nums: List[int]) -> List[int]:
    arr = cyclic_sort(nums)
    ans = []
    print(arr)
    for i in range(0, len(arr)):
        if i != arr[i] - 1:
            ans.append(i + 1)

    return ans


def cyclic_sort(arr):
    i = 0

    while i < len(arr):
        correct_index = arr[i] - 1
        if arr[i] != arr[correct_index]:
            swap(arr, i, correct_index)
        else:
            i += 1

    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(missingNumber(nums=arr))
