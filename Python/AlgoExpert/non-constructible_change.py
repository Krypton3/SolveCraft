# https://www.algoexpert.io/questions/non-constructible-change
def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for c in coins:
        if c > change + 1:
            break
        change += c
    return change + 1
