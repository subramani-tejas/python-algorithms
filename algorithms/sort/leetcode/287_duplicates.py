# https://leetcode.com/problems/find-the-duplicate-number/submissions/
from typing import List


class Solution:
    def findDuplicate(nums: List[int]):
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

        return ans[0]

    arr = [1, 3, 4, 2, 1, 5]
    print(findDuplicate(nums=arr))
