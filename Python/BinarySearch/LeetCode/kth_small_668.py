# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
def findKthNumber(m, n, k):
    def feasible(val):
        track = 0
        for i in range(1, m+1):
            find = min(val // i, n)
            if find == 0:
                break
            track += find
        return track >= k
    left, right = 1, m * n

    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
