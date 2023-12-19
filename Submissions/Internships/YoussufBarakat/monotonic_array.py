#1 - Definition : The array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.
#2 - Notes:
    #a) Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase.
    #b) Non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.
    #c) Empty arrays and arrays of one element are monotonic.

def isMonotonic(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or all(array[i] >= array[i + 1] for i in range(len(array) - 1))

print(isMonotonic([]))