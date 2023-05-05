def min_bracket_reversals(A):
    n = len(A)

    # if odd length - it can't be balanced
    if n % 2 != 0:
        print(-1)
        return -1

    map = {}
    for char in A:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    left = map.get('[', 0)
    right = map.get(']', 0)
    print("left [:", left)
    print("right ]:", right)

    print(abs(left - right) // 2)
    return abs(left - right) // 2


def min_reversals(A):
    count = 0
    for char in A:
        if char == '[':
            count += 1
        elif char == ']':
            count -= 1

    print("min_reversals answer is:", count)
    return count


# A = '[[][][]]]]]]'
# A = ']]][][[][][[[['

# how is expected=3?
A = "]]][][[][]"

min_bracket_reversals(A)
min_reversals(A)
