# https://leetcode.com/problems/search-insert-position/
def searchInsert(nums, target):
    def condition(val, target):
        if nums[val] > target:
            return True
        return False
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if condition(mid, target):
            right = mid
        else:
            left = mid + 1
    return left
