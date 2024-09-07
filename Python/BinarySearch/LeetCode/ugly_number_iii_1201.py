# https://leetcode.com/problems/ugly-number-iii/description/
import math


def nthUglyNumber(n, a, b, c):
    def feasible(val):
        total = val // a + val // b + val // c - val // ab - val // ac -\
            val // bc + val // abc
        return total >= n
    ab = a * b // math.gcd(a, b)
    ac = a * c // math.gcd(a, c)
    bc = b * c // math.gcd(b, c)
    abc = a * bc // math.gcd(a, bc)
    left, right = 1, 10 ** 10
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
