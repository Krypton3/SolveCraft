'''
Find the maximum sum of k consecutive elements in an array.
'''


def max_sum_subarray(nums, sliding_window):
    # find the initial sum of the sliding window
    value = sum(nums[:sliding_window])
    max_sum = value

    # sliding window from left to right
    for i in range(1, len(nums) - sliding_window + 1):
        value = value - nums[i-1] + nums[i+sliding_window-1]
        max_sum = max(value, max_sum)
    return max_sum


arr = [2, 3, 5, 8, 9, 10]
sliding_window = 3
print("maximum sum of k consecutive elements in an array is: ",
      max_sum_subarray(arr, sliding_window))
