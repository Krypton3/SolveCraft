# check if a number is palindrome
def palindrom_number(number):
    check = number
    reverse_sum = 0
    while number != 0:
        digit = number % 10
        reverse_sum = reverse_sum * 10 + digit
        number = number // 10
    if check == reverse_sum:
        print("Palindrome")
    else:
        print("Not Palindrome")


palindrom_number(12321)
