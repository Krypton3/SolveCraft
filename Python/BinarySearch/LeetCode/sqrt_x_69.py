# https://leetcode.com/problems/sqrtx/
def mySqrt(x):
    def condition(mid, x):
        if mid * mid > x:
            return True
        return False

    left, right = 0, x + 1
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid, x):
            right = mid
        else:
            left = mid + 1
    return left - 1
