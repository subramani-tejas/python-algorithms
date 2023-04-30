import my_sclr.day_9_subarray.subarray_sums as subarray
import my_sclr.day_7_prefix.prefix_sum as prefix_sum
import frequency as freqMap


# O(N^3)
def initialSubarrayZeroSum(arr):
    n = len(arr)

    # find all subarrays
    # O(N^3)
    allSubarrays = subarray.getAllSubArrays(arr)

    # count of subarrays with sum=0
    count = 0
    for sub in allSubarrays:
        sum = 0
        for item in sub:
            sum += item
        if sum == 0:
            count += 1
            print(sub)

    return count


# O(N)
# BUG
def subarrayZeroSum(arr):
    psum = prefix_sum.get_prefix_sum(arr)  # O(N)
    map = freqMap.getElementFrequency(psum)  # O(N)
    mySet = set(map)

    count = 0
    count = 1 if psum[len(arr) - 1] == 0 else 0

    # using set
    # for i in range(len(psum)):
    #     if psum[i] == 0 or mySet.__contains__(psum[i]):
    #         count += 1
    #     mySet.add(psum[i])

    # using hashmap
    for key, value in map.items():
        if key != 0 and value > 1:
            count += 1
        if key == 0:
            count += value

    return count


# arr = [2, 8, -10, 1]
# arr = [2, 2, 1, -3, 4, 3, 1, -2, -3, 2, 1]
arr = [2, -5, 3, 6, -6, -2, 2]

print("brute force count:", initialSubarrayZeroSum(arr))
print("psum optimized count:", subarrayZeroSum(arr))
