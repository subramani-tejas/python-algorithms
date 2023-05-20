def maximum_wealth(accounts):
    """ LeetCode: 1672. Richest Customer Wealth
    You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
    the ith customer has in the jth bank. Return the wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their bank accounts.
    The richest customer is the customer that has the maximum wealth.

    Input: accounts = [[1,5],[7,3],[3,5]]
    Output: 10
    Explanation:
    1st customer has wealth = 6
    2nd customer has wealth = 10
    3rd customer has wealth = 8
    The 2nd customer is the richest with a wealth of 10.
    """
    max_wealth = 0

    """ Simple row sum. O(row * col) """
    for row in accounts:
        sum_wealth = 0
        for item in row:
            sum_wealth += item
            if sum_wealth > max_wealth:
                max_wealth = sum_wealth

    # return max_wealth

    # return max(sum(row) for row in accounts)

    """ Using map(). (row * col) """
    wealth = list(map(sum, accounts))
    return max(wealth)


def shuffle(nums, n):
    """ LeetCode: 1470. Shuffle the Array
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7]
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
    """

    """ O(N/2) ==> O(N) """
    n = len(nums) // 2
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i + n])

    return res


def kids_with_candies(candies, extra_candies):
    """ LeetCode: 1431. Kids With the Greatest Number of Candies
    There are n kids with candies. You are given an integer array candies, where each candies[i]
    represents the number of candies the ith kid has, and an integer extra_candies, denoting the
    number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, after giving the ith
    kid all the extraCandies, they will have the greatest number of candies among all the kids,
    or false otherwise. Note that multiple kids can have the greatest number of candies.

    Input: candies = [2,3,5,1,3], extra_candies = 3
    Output: [true,true,true,false,true]

    Explanation: If you give all extraCandies to:
    - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
    - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
    - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
    - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    """
    result = []
    max_candy = max(candies)

    """ O(N) """
    for kid in candies:
        new_candies = kid + extra_candies
        if new_candies >= max_candy:
            result.append(True)
        else:
            result.append(False)

    """ Alternate solution.  
    [kid + extra_candies >= max_candy for kid in candies]
    """

    return result


def num_identical_pairs(nums):
    """ LeetCode: 1512. Number of Good Pairs
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    Input: nums = [1, 2, 3, 1, 1, 3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
    """

    """ O(N^2) """
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                count += 1

    """ O(N) | O(N) """
    count_ = 0
    freq = {}

    for item in nums:
        if item not in freq:
            freq[item] = 1
        else:
            freq[item] += 1
            count_ += freq[item]

    return count_


def smaller_numbers_than_current(arr):
    """ LeetCode: 1365. How Many Numbers Are Smaller Than the Current Number Given the
    array nums, for each nums[i] find out how many numbers in the array are smaller than it.
    That is, for each nums[i] you have to count the number of valid j's such that
    j != i and nums[j] < nums[i]. Return the answer in an array.

    Example 1:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Explanation:
    For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
    For nums[1]=1 does not exist any smaller number than it.
    For nums[2]=2 there exist one smaller number than it (1).
    For nums[3]=2 there exist one smaller number than it (1).
    For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

    Example 2:
    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]

    Example 3:
    Input: nums = [7,7,7,7]
    Output: [0,0,0,0]
    """

    """ Using prefix sum | count sort | TC: O(N + max_element) | SC: O(N)
    Count the frequency of each element in the array and then calculate
    the prefix sum of the frequency array. The prefix sum array will give you
    the number of elements smaller than the current element.
    """
    n = len(arr)
    res = [0] * n
    freq = [0] * (max(arr) + 1)

    for element in arr:
        freq[element] += 1

    freq_prefix_sum = [freq[0]]
    for i in range(1, len(freq)):
        freq_prefix_sum.append(freq[i] + freq_prefix_sum[i - 1])

    print(freq_prefix_sum)

    for i in range(n):
        if arr[i] != 0:
            res[i] = freq_prefix_sum[arr[i] - 1]

    return res

    # noinspection PyUnreachableCode
    """ Brute force. O(N^2) 
            n = len(arr)
            res = [0] * n
        
            for i in range(n):
                for j in range(n):
                    if arr[j] < arr[i]:
                        res[i] += 1
        
            return res
        """
