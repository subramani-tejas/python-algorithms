# 1929. Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/

import enum


def get_concatenation(nums):
    ans = [0] * (len(nums)*2)
    for i in range(len(nums)):
        ans[i] = nums[i]
        ans[i+len(nums)] = nums[i]
    return ans

    # return nums * 2


input = [1, 2, 1]
# print(get_concatenation(input))


# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. Define a running sum array as
# runningSum[i] = sum(nums[0]…nums[i])


def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums


nums = [1, 2, 3, 4]
# print(running_sum(nums))


# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

def maximum_wealth(accounts):
    wealth = []
    for customer in accounts:
        wealth.append(sum(customer))

    return max(wealth)


accounts = [[1, 5], [7, 3], [3, 5]]
# print(maximum_wealth(accounts))


# 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(nums):
    n = len(nums)
    ans = []
    x = 0
    y = n//2

    while(x < n//2 and y < n):
        ans.append(nums[x])
        ans.append(nums[y])
        x += 1
        y += 1

    return ans


nums = [2, 5, 1, 3, 4, 7]
# print(shuffle(nums))


# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
def kidsWithCandies(candies, extraCandies):
    max_candy = max(candies)
    # res = []

    # for kid in candies:
    #     if(kid + extraCandies >= max_candy):
    #         res.append(True)
    #     else:
    #         res.append(False)

    return [kid + extraCandies >= max_candy for kid in candies]


candies = [2, 3, 5, 1, 3]
extraCandies = 3
# print(kidsWithCandies(candies, extraCandies))


# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums):
    count = 0
    dict1 = {}
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if nums[i] == nums[j] and i < j:
    #             count += 1

    # using dictionary
    for number in nums:
        if number in dict1:
            count += dict1[number]
            dict1[number] += 1
        else:
            dict1[number] = 1

    return count


nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))
