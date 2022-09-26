# https://leetcode.com/problems/find-the-duplicate-number/submissions/
from typing import List


class Solution:
    def findDuplicate(nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                ci = nums[i] - 1
                if nums[i] != nums[ci]:
                    nums[i], nums[ci] = nums[ci], nums[i]
                else:
                    return nums[i]
            else:
                i += 1

        return -1

    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDuplicate(nums=arr))
