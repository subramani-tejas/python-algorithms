def base10_base2(n):
    ans = ""

    while n > 1:
        r = n % 2
        ans = ans + str(r)

        n = n // 2
        if n == 1:
            ans = ans + str(n)

    return reverse_string(ans)


def reverse_string(s):
    i, rev = len(s) - 1, ""
    while i >= 0:
        rev = rev + s[i]
        i -= 1

    return rev


print(base10_base2(12))
