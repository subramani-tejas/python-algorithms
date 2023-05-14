# O(N^2)
def find_all_subarrays_with_min_max(arr):
    max_ = max(arr)
    min_ = min(arr)
    n = len(arr)
    all_subarrays = []

    for i in range(n):
        if arr[i] == max_:
            for j in range(i + 1, n):
                if arr[j] == min_:
                    all_subarrays.append([i, j])
                # if arr[j] == max_:
                #     i = j

        if arr[i] == min_:
            for j in range(i + 1, n):
                if arr[j] == max_:
                    all_subarrays.append([i, j])
                # if arr[j] == min_:
                #     i = j

    return all_subarrays


def find_smallest_subarray_min_max(arr):
    all_subarrays = find_all_subarrays_with_min_max(arr)
    print(all_subarrays)
    for i, j in all_subarrays:
        for x in range(i, j + 1):
            print(arr[x], end=" ")
        print(f" ======== for {i}, {j}")

    return 0


# O(N)
def optimized(arr):
    n = len(arr)
    least_max_index, least_min_index = -1, -1
    ans = n
    max_, min_ = max(arr), min(arr)

    for i in range(n):
        if arr[i] == max_:
            least_max_index = i
            if least_min_index >= 0:
                # print(least_max_index, least_min_index)
                ans = min(ans, i - least_min_index + 1)

        if arr[i] == min_:
            least_min_index = i
            if least_max_index >= 0:
                # print(least_min_index, least_max_index)
                ans = min(ans, i - least_max_index + 1)

    return ans


nums = [2, 2, 6, 4, 5, 1, 5, 2, 6, 4, 1]
# arr = [1, 2, 3, 1, 3, 4, 6, 4, 6, 3]
# find_smallest_subarray_min_max(arr)

# arr = [7, 7, 7, 7, 7, 7]
print(optimized(nums))
