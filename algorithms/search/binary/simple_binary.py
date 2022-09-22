from typing import List


def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    comparison_count = 0

    while start <= end:
        mid = start + ((end - start) // 2)
        comparison_count += 1

        if key == arr[mid]:
            return mid, comparison_count
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
key = 11
res, comparisons = binary_search(arr, key)
print("target at index:", res)
print("comparisons:", comparisons)


# leetcode 744
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target < letters[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return letters[start % len(letters)]
