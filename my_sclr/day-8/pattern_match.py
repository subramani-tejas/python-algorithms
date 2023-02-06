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


def count_ag2(text):
    count_a = 0
    ans = 0
    for char in text:
        if char == 'a':
            count_a += 1
        if char == 'g':
            ans += count_a
    return ans


s = "bcaggaag"
x = count_ag2(s)
print(x)
