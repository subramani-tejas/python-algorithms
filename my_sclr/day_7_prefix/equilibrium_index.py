# equilibrium index of an array
# sum of elements on left of EI = sum of elements on right of EI
import prefix_sum


def get_ei_count(arr):
    count = 0
    left_sum, right_sum = [0] * len(arr), [0] * len(arr)

    # O(N)
    psum = prefix_sum.get_prefix_sum(arr)

    # O(N)
    for i in range(len(arr)):
        left_sum[i] = psum[i] - arr[i]
        right_sum[i] = psum[len(arr) - 1] - psum[i]

    # O(N)
    for i in range(len(arr)):
        if left_sum[i] == right_sum[i]:
            count += 1

    return count


def get_EI(arr):
    psum = prefix_sum.get_prefix_sum(arr)
    i = 0
    ei = []

    while i < len(arr):
        if psum[i] == (psum[len(arr) - 1] + arr[i]) // 2:
            ei.append(i)
        i += 1

    return min(ei) if ei else -1


nums = [-7, 1, 5, 2, -4, 3, 0]
# nums = [-3, 2, 4, -1]


print(get_ei_count(nums))
