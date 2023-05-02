# You are given a string S, and you have to find all the amazing substrings of S.
# An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
#
# Input: Only argument given is string S.
# Output: Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
VOWELS = ['a', 'e', 'i', 'o', 'u']


def findAllSubarraysStartVowel(S):
    n = len(S)
    allS = []

    for i in range(n):
        if S[i].lower() in VOWELS:
            for j in range(i, n):
                sub = []
                for k in range(i, j + 1):
                    sub.append(S[k])
                allS.append(sub)

    print(allS)
    return len(allS) % 10003


def findAmazingSubarrayCount(S):
    n = len(S)
    count = 0

    for i in range(n):
        if S[i].lower() in VOWELS:
            count += n - i

    print(count)
    return count


S = "ABEcU"
findAllSubarraysStartVowel(S)
findAmazingSubarrayCount(S)
