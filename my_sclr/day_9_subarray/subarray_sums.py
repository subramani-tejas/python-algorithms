import my_sclr.day_7_prefix.prefix_sum as prefix_sum


# O(N^3)
def getAllSubArrays(arr):
    n = len(arr)
    # [[2], [2, 8], [2, 8, 9], [8], [8, 9], [9]]
    res = []
    for i in range(n):
        for j in range(i, n):
            ans = []
            for k in range(i, j + 1):
                ans.append(arr[k])
            res.append(ans)

    return res


# O(N^3)
def sumOfAllSubarrays(arr):
    allSubArrays = getAllSubArrays(arr)
    allSum = []
    for array in allSubArrays:
        sum = 0
        for item in array:
            sum += item
        allSum.append(sum)

    return allSum


# O(N^2)
def sumAllSubarraysPrefixSum(arr):
    n = len(arr)
    psum = prefix_sum.get_prefix_sum(arr)
    allSum = []

    for i in range(n):
        for j in range(i, n):
            sum_ = 0
            if i > 0:
                sum_ = psum[j] - psum[i - 1]
            else:
                sum_ = psum[j]
            allSum.append(sum_)

    return allSum


def getTotalSumOfAllSubarraysSum(arr):
    sumSubarrays = sumAllSubarraysPrefixSum(arr)
    sum = 0
    for item in sumSubarrays:
        sum += item
    return sum


arr = [3, 2, -1, 5]
getAllSubArrays(arr)
# print(sumOfAllSubarrays(arr))
# print(sumAllSubarraysPrefixSum(arr))
print(getTotalSumOfAllSubarraysSum(arr))
