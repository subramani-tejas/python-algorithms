def bubble_sort(arr):
    comparisons, swaps = 0, 0
    swapped = False
    for i in range(0, len(arr)):
        swapped = False
        for j in range(1, len(arr) - i):
            print("comparing:", arr[j - 1], "and", arr[j])
            comparisons += 1
            if arr[j - 1] > arr[j]:
                swap(arr, j - 1, j)
                swapped = True
        # if you didn't swap for i value => array is sorted
        if not swapped:
            break

    print(arr)
    print("comparisons", comparisons)
    print("swaps", swaps)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [1, 2, 3, 4]
bubble_sort(arr)
