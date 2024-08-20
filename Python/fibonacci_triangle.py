'''
A program to generate fibonacci triangle
'''


def fibonacci_triangle(n):
    a, b = 0, 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(b)
            a, b = b, a + b
        # Print the row as a space-separated string
        print(" ".join(map(str, row)))


fibonacci_triangle(10)
