# Given an array A of N integers. Count the number of elements that have at least 1 elements greater than itself.
def solve(arr):
    max_ = arr[0]
    for item in arr:
        if item > max_:
            max_ = item

    count = 0
    for item in arr:
        if item != max_:
            count = count + 1
    return count


A = [3, 1, 2]
print(solve(A))
