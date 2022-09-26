# https://leetcode.com/problems/find-all-duplicates-in-an-array/

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

        return ans

    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDuplicate(nums=arr))
