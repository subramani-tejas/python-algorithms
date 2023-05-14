# Find the number of leaders in the array
# Leader: An element is greater than all the elements on its left side
# a[i] > a[0, i-1]

# O(N^2)
def initial_find_leaders(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        leader = True
        for j in range(i):
            # not a leader
            if arr[j] >= arr[i]:
                leader = False
        if leader:
            count += 1

    return count


# O(N)
def optimized_find_leaders(arr):
    n = len(arr)
    max_so_far = arr[0]
    count = 1

    for i in range(1, n):
        if arr[i] > max_so_far:
            max_so_far = arr[i]
            count += 1

    return count


numbers = [2, 5, 3, 4, 17, 16]
optimized_find_leaders(numbers)
