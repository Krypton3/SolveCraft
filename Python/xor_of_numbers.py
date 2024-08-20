'''
Given two number, find the XOR
'''


def convert(number):
    # conver number to binary
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary


def calculate_xor(x, y):
    # finding the proper binary number
    first = convert(max(x, y))
    second = convert(min(x, y))
    extra_size = len(first) - len(second)
    if extra_size > 0:
        second = "0" * extra_size + second
    # Calculate XOR
    xor_value = ""
    for i, j in zip(first, second):
        xor_value += "1" if i != j else "0"
    print("xor string: ", xor_value)
    # Convert XOR binary string to decimal
    res = int(xor_value, 2)

    print("The XOR of the given number is: ", res)


calculate_xor(5, 75)
