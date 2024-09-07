# https://leetcode.com/problems/koko-eating-bananas/description/
from math import ceil


def minEatingSpeed(piles, h):
    def feasible(val):
        hour_count = 0
        for p in piles:
            if p <= val:
                hour_count += 1
            else:
                hour_count += ceil(p/val)
        if hour_count <= h:
            return True
        else:
            return False

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
