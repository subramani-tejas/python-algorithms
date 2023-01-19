def flatten1(arr):
    print(f"this is input: {arr}")
    ans = []
    for i in range(len(arr) - 1):
        flatten2(arr[i], arr[i + 1])
        ans.append(arr[i])
    print(f"this is output: {ans}")


def flatten2(a1, a2):
    if a2[0] <= a1[1]:
        a1[1] = a2[1]
    return a1


arr = [[0, 540], [540, 630], [720, 780], [960, 1080], [1010, 1439]]
a1 = [0, 540]
a2 = [540, 630]
flatten1(arr)
