'''
https://leetcode.com/problems/string-to-integer-atoi/description/
Implement the myAtoi(string s) function, which converts a string to a 32-bi
signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character
is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit
character is encountered or the end of the string is reached. If no digits
were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range
[-231, 231 - 1], then round the integer to remain in the range. Specifically,
integers less than -231 should be rounded to -231, and integers greater than
231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
'''


def myAtoi(self, s: str) -> int:
    sign = 0
    digit = 0
    result = "0"
    s = s.strip()
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122 or\
             ord(i) == 46:
            break
        elif ord(i) == 32:
            break
        elif ord(i) == 43 or ord(i) == 45:
            if digit > 0 or sign != 0:
                break
            else:
                sign = -1 if ord(i) == 45 else +1
        else:
            if ord(i) == 48 and len(result) == 0:
                continue
            result += i
            digit += 1
    result = sign * int(result) if sign != 0 else int(result)
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    elif result > INT_MAX:
        return INT_MAX
    else:
        return result
