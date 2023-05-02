# Given a number A. Return square root of the number if it is perfect square otherwise return -1.

# square root if only num is perfect square
# O(sqrt(num))
def findSqRoot(num):
    i = 1
    ans = -1

    while i * i <= num:
        if i * i == num:
            ans = i
        i += 1

    return ans


# square root using binary search
# O(log N)
def findSqRootBinary(num):
    if num < 2:
        return 1

    start, end = 1, num

    while start <= end:
        mid = start + (end - start) // 2
        potential_square = mid * mid

        if potential_square == num:
            return mid
        elif potential_square > num:
            end = mid - 1
        else:
            start = mid + 1

    return -1
