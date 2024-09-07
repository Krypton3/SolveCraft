# https://leetcode.com/problems/first-bad-version/description/
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
'''


def firstBadVersion(n):
    def isBadVersion(mid):
        pass
    left, right = 0, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
