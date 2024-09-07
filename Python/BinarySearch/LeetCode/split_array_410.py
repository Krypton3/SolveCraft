# https://leetcode.com/problems/split-array-largest-sum/description/
def splitArray(nums, k):
    def feasible(val):
        track = 0
        total = 0
        for i in nums:
            total += i
            if total > val:
                total = i
                track += 1
                if track >= k:
                    return False
        return True
    if len(nums) == k:
        return max(nums)
    left, right = max(nums), sum(nums)

    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
