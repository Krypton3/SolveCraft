# highest common factor or greatest common divisor
def hcf_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(hcf_gcd(48, 18))
