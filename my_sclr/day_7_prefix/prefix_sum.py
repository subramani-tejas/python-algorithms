# prefix sum in place

# TC: O(N + Q)
# SC: O(1)
def first_solution(arr, queries):
    ans = []

    for each_query in queries:
        L, R = each_query[0], each_query[1]
        my_sum = 0
        for i in range(L, R + 1):
            my_sum += arr[i]
        ans.append(my_sum)

    return ans


# O(N)
def get_prefix_sum_in_place(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]
    return arr


# O(N)
def get_prefix_sum(arr):
    prefix_sum = [arr[0]]
    for i in range(1, len(arr)):
        my_sum = arr[i] + prefix_sum[i - 1]
        prefix_sum.append(my_sum)
    return prefix_sum


# TC: O(N + Q)
# SC: O(N)
def query_range_sum(arr, queries):
    # prefix sum ==> [-3, 3, 5, 9, 14, 16, 24, 15, 18, 19]
    prefix_sum = get_prefix_sum(arr)
    ans = []
    for each_query in queries:
        left, right = each_query
        if left == 0:
            my_sum = prefix_sum[right]
        else:
            my_sum = prefix_sum[right] - prefix_sum[left - 1]
        ans.append(my_sum)
    return ans


nums = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
query = [[4, 8], [3, 7], [1, 3], [0, 4], [7, 7]]
# x = query_range_sum(arr, queries)

first_solution(nums, query)
get_prefix_sum(nums)
get_prefix_sum_in_place(nums)
