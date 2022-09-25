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


# leetcode 33
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_index = self.peakIndexInMountainArray(nums)
        try_once = self.ascending_binary_search(nums, target, 0, pivot_index)
        if try_once != -1:
            return try_once

        return self.descending_binary_search(nums, target, pivot_index + 1, len(nums) - 1)

    def peakIndexInMountainArray(arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        while start != end:
            mid = start + ((end - start) // 2)
            if arr[mid] > arr[mid + 1]:
                end = mid
            elif arr[mid] < arr[mid + 1]:
                start = mid + 1

        return start

    def descending_binary_search(self, arr, key, start, end):
        while start <= end:
            mid = start + ((end - start) // 2)

            if key == arr.get(mid):
                return mid
            elif key < arr.get(mid):
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def ascending_binary_search(self, arr, key, start, end):
        while start <= end:
            mid = start + ((end - start) // 2)

            if key == arr.get(mid):
                return mid
            elif key > arr.get(mid):
                start = mid + 1
            else:
                end = mid - 1

        return -1
