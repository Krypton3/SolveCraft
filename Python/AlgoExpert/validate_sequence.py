# https://www.algoexpert.io/questions/validate-subsequence
def isValidSubsequence(array, sequence):
    # Write your code here.
    j = 0
    cnt = 0
    for i in array:
        if j < len(sequence) and i == sequence[j]:
            j += 1
            cnt += 1

    return cnt == len(sequence)
