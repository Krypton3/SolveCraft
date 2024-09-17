# https://www.geeksforgeeks.org/number-subarrays-sum-exactly-equal-k/
def subArraySum(arr, k):
    res = 0
    diff = {}
    prefix_sum = 0
    for i in range(0, len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            res += 1

        if (prefix_sum - k) in diff:
            res += diff[prefix_sum - k]

        if prefix_sum in diff:
            diff[prefix_sum] += 1
        else:
            diff[prefix_sum] = 1
    return res


arr = [10, 2, -2, -20, 10]
Sum = -10
print(subArraySum(arr, Sum))
