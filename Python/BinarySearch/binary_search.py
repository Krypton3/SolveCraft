def binary_search(arr, target):
    left, right = min(arr), max(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 4))
