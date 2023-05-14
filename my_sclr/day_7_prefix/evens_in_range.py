# array with N elements & Q queries
# for each query [L, R] find count of even numbers in that range
import prefix_sum


# O(N)
def get_num_evens(arr, queries):
    evens = get_evens(arr)
    return get_range_sum(evens, queries)


def get_range_sum(arr, queries):
    psum_evens = prefix_sum.get_prefix_sum_in_place(arr)
    ans = []

    for query in queries:
        left, right = query
        if left == 0:
            my_sum = psum_evens[right]
        else:
            my_sum = psum_evens[right] - psum_evens[left - 1]
        ans.append(my_sum)
    return ans


# O(N)
def get_evens(arr):
    evens = []
    for item in arr:
        if item % 2 == 0:
            evens.append(1)
        else:
            evens.append(0)
    return evens


# arr = [2, 1, 8, 3, 9, 6]
# queries = [[0, 3], [3, 5], [1, 3], [2, 4]]

nums = [2, 4, 3, 7, 9, 8, 6, 5, 4, 9]
all_queries = [[4, 8], [3, 9], [0, 4]]

x = get_num_evens(nums, all_queries)
print(x)
