# https://www.algoexpert.io/questions/sorted-squared-array
def sortedSquaredArray(array):
    # Write your code here.
    sol = [0] * (len(array))
    print(sol)
    i, j = 0, len(array) - 1
    track = j
    while track > -1:
        val1 = array[i]**2
        val2 = array[j]**2
        print(val1, val2, track)

        if val2 > val1:
            sol[track] = val2
            j -= 1
        else:
            sol[track] = val1
            i += 1
        track -= 1
    return sol
