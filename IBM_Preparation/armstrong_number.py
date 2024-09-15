# Write a function that can validate if a number is Armstrong number or not
def check_armstrong(number):
    n = len(str(number))
    check = number
    sum = 0

    while number > 0:
        digit = number % 10
        sum += digit ** n
        number = number // 10
    if sum == check:
        print("This is an armstrong number: ", sum)
    else:
        print("This is not an armstrong number")


check_armstrong(153)
