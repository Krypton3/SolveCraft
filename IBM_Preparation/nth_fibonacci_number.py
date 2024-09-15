# Write a function that produces nth fibonacci number
def nth_fibonacci(n):
    if n <= 1:
        return n
    return nth_fibonacci(n-1) + nth_fibonacci(n-1)


print("Nth fibonacci number: ", nth_fibonacci(10))
