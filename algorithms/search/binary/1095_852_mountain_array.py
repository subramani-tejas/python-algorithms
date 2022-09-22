# leetcode 1095
# https://leetcode.com/problems/find-in-mountain-array/
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak_index = self.peakIndexInMountainArray(arr=mountain_arr)
        try_once = self.ascending_binary_search(mountain_arr, target, 0, peak_index)
        if try_once != -1:
            return try_once

        return self.descending_binary_search(mountain_arr, target, peak_index + 1, mountain_arr.length() - 1)

    # get the middle index of the mountain array
    def peakIndexInMountainArray(self, arr):
        start, end = 0, arr.length() - 1

        while start != end:
            mid = start + ((end - start) // 2)
            if arr.get(mid) > arr.get(mid + 1):
                end = mid
            elif arr.get(mid) < arr.get(mid + 1):
                start = mid + 1

        return start

    # ascending binary search
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

    # descending binary search
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

    
"""

"""
# leetcode 852
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    start, end = 0, len(arr) - 1

    while start != end:
        mid = start + ((end - start) // 2)
        if arr[mid] > arr[mid + 1]:
            end = mid
        elif arr[mid] < arr[mid + 1]:
            start = mid + 1

    return start


arr = [1, 2, 3, 5, 6, 4, 3, 2]
res = peakIndexInMountainArray(arr=arr)
print(res)
