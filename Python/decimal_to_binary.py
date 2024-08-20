'''
Write a Program to Change Decimal Number to Binary?
'''


def convert(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary


print("Decimal to Binary: ", convert(75))
