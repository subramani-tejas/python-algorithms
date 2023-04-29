# given string 's' of lower case alphabets,
# return count of [i, j] such that:
# i < j
# s[i] => 'a'
# s[j] => 'g'

# O(N^2)
def count_ag(text):
    n = len(text)
    count = 0

    for i in range(n):
        if s[i] == 'a':
            for j in range(i + 1, n):
                if s[j] == 'g':
                    count += 1

    return count


# O(N)
def count_ag2(text):
    carry = 0
    ans = 0
    for char in text:
        if char == 'a':
            carry += 1
        if char == 'g':
            ans += carry
    return ans


s = "aabegaag"
x = count_ag2(s)
print(x)
