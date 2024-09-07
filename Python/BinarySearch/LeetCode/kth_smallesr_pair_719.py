# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
def smallestDistancePair(nums, k):
    nums.sort()
    n = len(nums)
    left, right = 0, nums[-1] - nums[0]

    def feasible(val):
        cnt, i, j = 0, 0, 0
        while i < n or j < n:
            while j < n and nums[j] - nums[i] <= val:
                j += 1
            cnt += j - i - 1
            i += 1
        return cnt >= k
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
