# You are given a string S, and you have to find all the amazing substrings of S.
# An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
#
# Input: Only argument given is string S.
# Output: Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
VOWELS = ['a', 'e', 'i', 'o', 'u']


def find_all_subarrays_start_vowel(s):
    n = len(s)
    allS = []

    for i in range(n):
        if s[i].lower() in VOWELS:
            for j in range(i, n):
                sub = []
                for k in range(i, j + 1):
                    sub.append(s[k])
                allS.append(sub)

    print(allS)
    return len(allS) % 10003


def find_amazing_subarray_count(s):
    n = len(s)
    count = 0

    for i in range(n):
        if s[i].lower() in VOWELS:
            count += n - i

    print(count)
    return count


S = "ABEcU"
find_all_subarrays_start_vowel(S)
find_amazing_subarray_count(S)
