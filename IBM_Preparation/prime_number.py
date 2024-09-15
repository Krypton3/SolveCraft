import math


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def print_primes_up_to_n(N):
    for num in range(2, N + 1):
        if is_prime(num):
            print(num, end=" ")


N = 50
print(f"Prime numbers less than or equal to {N}:")
print_primes_up_to_n(N)
