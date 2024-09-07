# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
def shipWithinDays(weights, days):
    def feasible(val):
        day = 1
        total = 0
        for w in weights:
            total += w
            if total > val:
                total = w
                day += 1
                if day > days:
                    return False
        return True
    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
