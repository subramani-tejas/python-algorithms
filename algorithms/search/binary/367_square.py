# https://leetcode.com/problems/valid-perfect-square/description/


def isPerfectSquare(self, num: int) -> bool:
    if num < 2:
        return True

    start, end = 1, num

    while start <= end:
        mid = start + (end - start) // 2
        potential_square = mid * mid

        if potential_square == num:
            return True
        elif potential_square > num:
            end = mid - 1
        else:
            start = mid + 1

    return False
