# https://leetcode.com/problems/set-mismatch/
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i, ans = 0, []

        while i < len(nums):
            ci = nums[i] - 1
            if nums[i] != nums[ci]:
                nums[i], nums[ci] = nums[ci], nums[i]
            else:
                i += 1

        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                ans.append(nums[i])
                ans.append(i + 1)

        return ans
