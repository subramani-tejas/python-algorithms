# array with N elements & Q queries
# for each query [L, R] find count of even numbers in that range

def get_num_evens(arr, queries):
    evens = get_evens(arr)
    return get_range_sum(evens, queries)


def get_range_sum(arr, queries):
    psum_evens = get_prefix_sum_in_place(arr)
    ans = []

    for query in queries:
        left, right = query
        if left == 0:
            sum = psum_evens[right]
        else:
            sum = psum_evens[right] - psum_evens[left - 1]
        ans.append(sum)
    return ans


def get_evens(arr):
    evens = []
    for item in arr:
        if item % 2 == 0:
            evens.append(1)
        else:
            evens.append(0)
    return evens


def get_prefix_sum_in_place(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] + arr[i]
    return arr


arr = [2, 1, 8, 3, 9, 6]
queries = [[0, 3], [3, 5], [1, 3], [2, 4]]

x = get_num_evens(arr, queries)
print(x)
