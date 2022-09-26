class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            correct_i = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[correct_i]:
                nums[i], nums[correct_i] = nums[correct_i], nums[i]
            else:
                i += 1

        for i in range(0, len(nums)):
            if i != nums[i]:
                return i

        return len(nums)
