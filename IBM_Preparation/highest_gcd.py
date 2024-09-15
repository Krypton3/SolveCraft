# Find GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of
# two numbers is the largest number that divides both of them.
def highest_gcd(a, b):
    min_val = min(a, b)
    while min_val > 0:
        if a % min_val == 0 and b % min_val == 0:
            return min_val
        min_val -= 1
    return -1


print(highest_gcd(48, 18))
