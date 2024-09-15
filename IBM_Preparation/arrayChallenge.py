'''
For each element of an array. a counter is set to 0.
the element is compared to each element to its left. if the
element to the left is greater, the absolute difference is substructed
fom the counter. if the element to the left is less, the absolute difference
is added to the counter. For each element of the array, determine
the value of the counter. These values should be stored in an array
and returned.

*** ALL the element to the left will be checked for every current element

n = 3
arr = [2, 4, 3]

answer: [0, 2, 0]

arr = [2, 1, 3]
answer: [0, -1, 3]
'''


def arrayChallenge(arr):
    if len(arr) <= 1:
        return [0]

    counters = [0] * len(arr)
    for i in range(1, len(arr)):
        counter = 0
        for j in range(i):
            if arr[j] > arr[i]:
                counter -= abs(arr[j] - arr[i])
            else:
                counter += abs(arr[j] - arr[i])
        counters[i] = counter

    return counters


def calculate_counters_optimized(arr):
    n = len(arr)
    if n <= 1:
        return [0]

    # Initialize the result array and the sum of elements to the left
    counters = [0] * n
    sum_left = arr[0]  # To track the sum of all elements to the left of arr[i]

    # Loop through each element starting from the second one
    for i in range(1, n):
        # Calculate the counter using the formula
        counters[i] = arr[i] * i - sum_left

        # After processing, update the sum of elements to the left for the
        # next iteration
        sum_left += arr[i]

    return counters


# Test cases
arr1 = [2, 4, 3]
print(calculate_counters_optimized(arr1))  # Expected output: [0, 2, 0]

arr2 = [2, 1, 3]
print(calculate_counters_optimized(arr2))  # Expected output: [0, -1, 3]
