'''
https://leetcode.com/problems/reverse-integer/description/
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
'''


def reverse(self, x: int) -> int:
    MIN_32_BIT = -2**31
    MAX_32_BIT = 2**31 - 1

    sign = -1 if x < 0 else 1
    number = abs(x)
    reverse = 0
    while number != 0:
        reverse = reverse * 10 + number % 10
        number //= 10
    actual_number = sign * reverse
    if MIN_32_BIT <= actual_number <= MAX_32_BIT:
        pass
    else:
        return 0
    return actual_number
