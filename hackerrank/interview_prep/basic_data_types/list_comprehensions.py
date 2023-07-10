# https://www.hackerrank.com/challenges/list-comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

res = [[i, j, k] for i in [a for a in range(x + 1)]
       for j in [b for b in range(y + 1)]
       for k in [c for c in range(z + 1)]
       if i + j + k != n
       ]
print(res)
