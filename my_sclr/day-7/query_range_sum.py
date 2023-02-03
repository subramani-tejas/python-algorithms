# Given array of N elements & Q queries,for each query,
# calculate sum of all elements in range [L, R].
# Return array with sum asked in each query range.

# TC: O(N*Q)
def solve(arr, queries):
    ans = []
    for query in queries:
        left, right = query
        sum = get_range_sum(arr, left, right)
        ans.append(sum)
    return ans


def get_range_sum(arr, left, right):
    sum = 0
    for i in range(left, right + 1):
        sum += arr[i]
    return sum


arr = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
queries = [[4, 8], [3, 7], [1, 3], [0, 4], [7, 7]]
ans = solve(arr, queries)
print(ans)
