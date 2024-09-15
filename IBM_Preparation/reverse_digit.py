# reverse a digit
def reverse_digit(number):
    result = ""
    while number > 0:
        result += str(number % 10)
        number = number // 10
    print(int(result))


reverse_digit(153)
