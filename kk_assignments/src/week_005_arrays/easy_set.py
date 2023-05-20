def maximum_wealth(accounts):
    """ LeetCode. 1672. Richest Customer Wealth
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
    """ 1470. Shuffle the Array
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
