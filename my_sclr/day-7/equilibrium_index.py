# equilibrium index of an array
# sum of elements on left of EI = sum of elements on right of EI

def get_prefix_sum(arr):
    psum = []
    psum.append(arr[0])
    for i in range(1, len(arr)):
        sum = psum[i - 1] + arr[i]
        psum.append(sum)
    return psum


def get_EI(arr):
    psum = get_prefix_sum(arr)
    i = 0
    ei = []

    while i < len(arr):
        if psum[i] == (psum[len(arr) - 1] + arr[i]) // 2:
            ei.append(i)
        i += 1

    return min(ei) if ei else -1


arr = -7, 1, 5, 2, -4, 3, 0
x = get_EI(arr)
print(x)
