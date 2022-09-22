def linear_search(arr: list, key: int) -> int:
    comparison_count = 0
    for i in range(0, len(arr)):
        comparison_count += 1
        if arr[i] == key:
            return i, comparison_count

    return -1, comparison_count


arr1 = [18, 12, 9, 14, 77, 50]
key1 = 505

res, comparisons = linear_search(arr=arr1, key=key1)
print("target at index: ", res)
print("comparisons: ", comparisons)
