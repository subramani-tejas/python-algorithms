# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent(nums):
    # ans = []

    # O(n^2)
    # for i in range(len(nums)):
    #     count = 0
    #     for j in range(len(nums)):
    #         if nums[i] > nums[j] and j != i:
    #             count += 1
    #     ans.append(count)

    # return ans

    # O(n) + O(n)
    sorted_nums = sorted(nums)
    map = {}
    for i in range(len(sorted_nums)):
        if sorted_nums[i] not in map:
            map[sorted_nums[i]] = i

    return [map[item] for item in nums]


nums = [8, 1, 2, 2, 3]
(smallerNumbersThanCurrent(nums))


# 1389. Create Target Array in the Given Order
# https://leetcode.com/problems/create-target-array-in-the-given-order/


def createTargetArray(nums, index):
    target = list()

    for i in range(len(nums)):
        target.insert(index[i], nums[i])

    return target


nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]

(createTargetArray(nums, index))


# 1832. Check if the Sentence Is Pangram
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

def checkIfPangram(sentence: str) -> bool:
    ALPHABET_SIZE = 26

    # O(n) - using data structure
    # if len(set(sentence)) == ALPHABET_SIZE:
    #     return True

    # return False

    found = []

    for letter in sentence:
        if letter not in found:
            found.append(letter)

    print(len(found))
    return len(found) == ALPHABET_SIZE


sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))
