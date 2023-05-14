import my_sclr.day_9_subarray.subarray_sums as subarray
import my_sclr.day_7_prefix.prefix_sum as prefix_sum
import frequency as freq_map


# O(N^3)
def initial_subarray_zero_sum(arr):
    # find all subarrays
    # O(N^3)
    allSubarrays = subarray.get_all_subarrays(arr)

    # count of subarrays with sum=0
    count = 0
    for sub in allSubarrays:
        my_sum = 0
        for item in sub:
            my_sum += item
        if my_sum == 0:
            count += 1
            print(sub)

    return count


# O(N)
# BUG
def subarray_zero_sum(arr):
    psum = prefix_sum.get_prefix_sum(arr)  # O(N)
    my_map = freq_map.get_element_frequency(psum)  # O(N)
    # mySet = set(map)

    # count = 0
    count = 1 if psum[len(arr) - 1] == 0 else 0

    # using set
    # for i in range(len(psum)):
    #     if psum[i] == 0 or mySet.__contains__(psum[i]):
    #         count += 1
    #     mySet.add(psum[i])

    # using hashmap
    for key, value in my_map.items():
        if key != 0 and value > 1:
            count += 1
        if key == 0:
            count += value

    return count


# nums = [2, 8, -10, 1]
# nums = [2, 2, 1, -3, 4, 3, 1, -2, -3, 2, 1]
nums = [2, -5, 3, 6, -6, -2, 2]

print("brute force count:", initial_subarray_zero_sum(nums))
print("psum optimized count:", subarray_zero_sum(nums))
