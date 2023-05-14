def min_bracket_reversals(a):
    n = len(a)

    # if odd length - it can't be balanced
    if n % 2 != 0:
        print(-1)
        return -1

    my_map = {}
    for char in a:
        if char in my_map:
            my_map[char] += 1
        else:
            my_map[char] = 1

    left = my_map.get('[', 0)
    right = my_map.get(']', 0)
    print("left [:", left)
    print("right ]:", right)

    print(abs(left - right) // 2)
    return abs(left - right) // 2


def min_reversals(a):
    count = 0
    for char in a:
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
