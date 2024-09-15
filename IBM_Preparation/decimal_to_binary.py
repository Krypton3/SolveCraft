# Write a Program to Change Decimal Number to Binary?
def conversion(number):
    res = ""
    while number > 0:
        res += str(number % 2)
        number = number // 2
    print(res[::-1])


conversion(100)
