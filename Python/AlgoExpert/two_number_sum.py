# https://www.algoexpert.io/questions/two-number-sum
def twoNumberSum(array, targetSum):
    array.sort()
    # Write your code here.
    i, j = 0, len(array) - 1
    sum = 0
    while i < j:
        sum = array[i] + array[j]
        print(sum, array[i], array[j])
        if sum == targetSum:
            return [array[i], array[j]]
        elif sum > targetSum:
            j -= 1
        else:
            i += 1
    return []
