# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
def minDays(bloomDay, m, k):
    def feasible(val):
        consequetive_flower = 0
        bouquet = 0
        for f in bloomDay:
            if f <= val:
                consequetive_flower += 1
                if consequetive_flower == k:
                    bouquet += 1
                    consequetive_flower = 0
            else:
                consequetive_flower = 0
            if bouquet >= m:
                return True
        return False

    if len(bloomDay) < (m * k):
        return -1
    left, right = min(bloomDay), max(bloomDay)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
