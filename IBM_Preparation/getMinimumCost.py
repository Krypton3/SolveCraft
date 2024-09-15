# https://leetcode.com/discuss/interview-question/1874750/
def getMinimumCost(arr):
    cost = 0
    max_cost = 0
    first_index, second_index = 0, 0

    # pair of max diff
    for i in range(len(arr) - 1):
        first_val = arr[i]
        second_val = arr[i + 1]
        if abs(second_val - first_val) > max_cost:
            max_cost = abs(second_val - first_val)
            first_index = i
            second_index = i + 1

    # we can just go for the mid value of the max diff
    mid = (arr[first_index] + arr[second_index]) // 2

    # get the cost of max diff position
    cost += (arr[first_index] - mid) ** 2
    cost += (arr[second_index] - mid) ** 2

    # calculate cost of the rest
    for i in range(len(arr) - 1):
        if i == first_index:
            continue  # skip max diff pair
        first_val = arr[i]
        second_val = arr[i + 1]
        cost += (first_val - second_val) ** 2

    return cost


# test case
# a = [1, 3, 5, 2, 10]
a = [10000, 9999, 8000, 5000, 10000, 2000]
print(getMinimumCost(a))
