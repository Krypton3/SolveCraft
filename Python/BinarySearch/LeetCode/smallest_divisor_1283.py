# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
def smallestDivisor(nums, threshold):
    def find(divisor):
        total_sum = 0
        for n in nums:
            total_sum += (n + divisor - 1) // divisor
        return total_sum <= threshold
    left, right = 1, max(nums)
    while left < right:
        mid = left + (right - left) // 2
        if find(mid):
            right = mid
        else:
            left = mid + 1
    return left
