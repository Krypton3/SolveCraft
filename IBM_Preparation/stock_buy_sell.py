# https://www.geeksforgeeks.org/stock-buy-sell/
def max_profit(arr):
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            profit += arr[i] - arr[i - 1]
    return profit


prices = [100, 180, 260, 310, 40, 535, 695]
print(max_profit(prices))
