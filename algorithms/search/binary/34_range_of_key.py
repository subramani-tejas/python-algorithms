# leetcode34
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


def search_range(self, arr: List[int], key: int) -> List[int]:
    first_occurence = binary_search(arr, key, first_index=True)
    last_occurence = binary_search(arr, key, first_index=False)

    return [first_occurence, last_occurence]


def binary_search(arr, key, first_index):
    start, end = 0, len(arr) - 1
    ans = -1

    while start <= end:
        mid = start + ((end - start) // 2)

        if key == arr[mid]:
            # potential ans
            ans = mid
            if first_index:
                end = mid - 1
            else:
                start = mid + 1

        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return ans
