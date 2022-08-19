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

    return len(found) == ALPHABET_SIZE


sentence = "thequickbrownfoxjumpsoverthelazydog"
(checkIfPangram(sentence))


# 1773. Count Items Matching a Rule
# https://leetcode.com/problems/count-items-matching-a-rule/
def countMatches(items, ruleKey, ruleValue):
    count = 0

    for item in items:
        if ruleKey == "type" and ruleValue == item[0]:
            count += 1
        if ruleKey == "color" and ruleValue == item[1]:
            count += 1
        if ruleKey == "name" and ruleValue == item[2]:
            count += 1

    return count


items = items = [["phone", "blue", "pixel"],
                 ["computer", "silver", "phone"],
                 ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"

(countMatches(items, ruleKey, ruleValue))


# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/
def largestAltitude(gain):
    n = len(gain)
    altitudes = [0] * (n+1)

    for i in range(n):
        altitudes[i+1] = altitudes[i] + gain[i]

    return max(altitudes)


gain = [-4, -3, -2, -1, 4, 3, 2]
print(largestAltitude(gain))


# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/
def flipAndInvertImage(image):
    pass


image = [[1, 1, 0],
         [1, 0, 1],
         [0, 0, 0]]
print(flipAndInvertImage(image))
