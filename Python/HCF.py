'''
Greatest Common Divisor of 2 Numbers
'''


def hcf(x, y):
    min_val = min(x, y)
    res = 0
    for i in range(1, min_val):
        if x % i == 0 and y % i == 0:
            res = i
    return res


print("Greatest Common Divisor is: ", hcf(70, 15))
