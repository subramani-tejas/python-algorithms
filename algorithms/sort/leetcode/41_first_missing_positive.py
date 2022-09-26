# https://leetcode.com/problems/first-missing-positive/
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            ci = nums[i] - 1
            if 0 < nums[i] < len(nums) and nums[i] != nums[ci]:
                nums[i], nums[ci] = nums[ci], nums[i]
            else:
                i += 1

        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
