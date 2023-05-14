import my_sclr.day_7_prefix.prefix_sum as prefix_sum


# O(N^3)
def get_all_subarrays(arr):
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
def sum_of_all_subarrays(arr):
    allSubArrays = get_all_subarrays(arr)
    allSum = []
    for array in allSubArrays:
        my_sum = 0
        for item in array:
            my_sum += item
        allSum.append(my_sum)

    return allSum


# O(N^2)
def sum_all_subarrays_prefix_sum(arr):
    n = len(arr)
    psum = prefix_sum.get_prefix_sum(arr)
    allSum = []

    for i in range(n):
        for j in range(i, n):
            if i > 0:
                sum_ = psum[j] - psum[i - 1]
            else:
                sum_ = psum[j]
            allSum.append(sum_)

    return allSum


def get_total_sum_of_all_subarrays_sum(arr):
    sumSubarrays = sum_all_subarrays_prefix_sum(arr)
    my_sum = 0
    for item in sumSubarrays:
        my_sum += item
    return my_sum


nums = [3, 2, -1, 5]
get_all_subarrays(nums)
# print(sumOfAllSubarrays(arr))
# print(sumAllSubarraysPrefixSum(arr))
# print(getTotalSumOfAllSubarraysSum(arr))
