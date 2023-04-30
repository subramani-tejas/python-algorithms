# prefix sum in place

# TC: O(N + Q)
# SC: O(1)
def first_solution(arr, queries):
    ans = []

    for query in queries:
        L, R = query[0], query[1]
        sum = 0
        for i in range(L, R + 1):
            sum += arr[i]
        ans.append(sum)

    return ans


# O(N)
def get_prefix_sum_in_place(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]
    return arr


# O(N)
def get_prefix_sum(arr):
    prefix_sum = []
    prefix_sum.append(arr[0])
    for i in range(1, len(arr)):
        sum = arr[i] + prefix_sum[i - 1]
        prefix_sum.append(sum)
    return prefix_sum


# TC: O(N + Q)
# SC: O(N)
def query_range_sum(arr, queries):
    # prefix sum ==> [-3, 3, 5, 9, 14, 16, 24, 15, 18, 19]
    psum = get_prefix_sum(arr)
    ans = []
    for query in queries:
        left, right = query
        if left == 0:
            sum = psum[right]
        else:
            sum = psum[right] - psum[left - 1]
        ans.append(sum)
    return ans


arr = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
queries = [[4, 8], [3, 7], [1, 3], [0, 4], [7, 7]]
# x = query_range_sum(arr, queries)

first_solution(arr, queries)
get_prefix_sum(arr)
get_prefix_sum_in_place(arr)
