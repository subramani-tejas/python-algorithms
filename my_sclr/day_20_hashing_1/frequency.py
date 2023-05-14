# find the frequency of each number queried
# O(N + Q) --- O(N)
def get_element_frequency(arr, q=None):
    frequencyMap = {}

    for item in arr:
        if item not in frequencyMap:
            frequencyMap[item] = 1
        else:
            frequencyMap[item] += 1

    queryFrequencies = []
    if q:
        for query in q:
            if query in frequencyMap:
                queryFrequencies.append(frequencyMap[query])
            else:
                queryFrequencies.append(0)
        return queryFrequencies

    return frequencyMap


numbers = [2, 6, 3, 8, 2, 8, 2, 3, 8, 10, 6]
Q = [2, 8, 3, 5, 6]

# get element freq count in query
x = get_element_frequency(numbers, Q)
print(x)

# get freq map
y = get_element_frequency(numbers)
print(y)
