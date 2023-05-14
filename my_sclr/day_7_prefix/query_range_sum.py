# Given array of N elements & Q queries,for each query,
# calculate sum of all elements in range [L, R].
# Return array with sum asked in each query range.

# TC: O(N * Q)
# SC: O(1)
def solve(arr, queries):
    ans = []
    for query in queries:
        left, right = query
        summ = get_range_sum(arr, left, right)
        ans.append(summ)
    return ans


def get_range_sum(arr, left, right):
    summ = 0
    for i in range(left, right + 1):
        summ += arr[i]
    return summ


nums = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
all_queries = [[4, 8], [3, 7], [1, 3], [0, 4], [7, 7]]
x = solve(nums, all_queries)
print(x)
