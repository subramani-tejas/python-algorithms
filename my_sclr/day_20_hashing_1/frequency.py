# find the frequency of each number queried
# O(N + Q) --- O(N)
def getElementFrequency(arr, Q=None):
    n = len(arr)
    frequencyMap = {}

    for item in arr:
        if item not in frequencyMap:
            frequencyMap[item] = 1
        else:
            frequencyMap[item] += 1

    queryFrequencies = []
    if Q:
        for query in Q:
            if query in frequencyMap:
                queryFrequencies.append(frequencyMap[query])
            else:
                queryFrequencies.append(0)
        return queryFrequencies

    return frequencyMap


arr = [2, 6, 3, 8, 2, 8, 2, 3, 8, 10, 6]
Q = [2, 8, 3, 5, 6]

# get element freq count in query
# x = getElementFrequency(arr, Q)
# print(x)
#
# # get freq map
# y = getElementFrequency(arr)
# print(y)
