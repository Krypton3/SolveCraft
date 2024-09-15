# find least common multiple
def hcf_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int((abs(a * b) / (hcf_gcd(a, b))))


print(lcm(12, 15))
