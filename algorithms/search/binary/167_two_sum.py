# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    start, end = 0, len(numbers) - 1

    while start <= end:
        sum = numbers[start] + numbers[end]
        if sum == target:
            return [start + 1, end + 1]
        elif sum > target:
            end -= 1
        else:
            start += 1

    return [-1, -1]
