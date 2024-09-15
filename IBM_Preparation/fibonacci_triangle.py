# Write a Program to generate Fibonacci Triangle.
def fibonacci_triangle(number):
    a, b = 0, 1  # Initial values of the Fibonacci sequence
    for i in range(1, number + 1):  # Loop through rows
        for j in range(i):  # Loop to print each value in a row
            print(a, end=" ")
            a, b = b, a + b  # Update to the next Fibonacci number
        print()  # Move to the next line after each row


fibonacci_triangle(10)
