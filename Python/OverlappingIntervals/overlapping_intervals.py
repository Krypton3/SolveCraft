def merged_intervals(intervals):
    if not intervals:
        return []

    # sort the intervals by their starting point
    intervals.sort(key=lambda x: x[0])

    # take the first interval as a starting point
    result = [intervals[0]]

    # Iterate through the sorted list
    for current_interval in intervals[1:]:
        # fetch the last interval from the result
        check_interval = result[-1]

        # check if the current interval overlaps the previous one.
        if current_interval[0] <= check_interval[1]:
            # overlap exists and merge the intervals by updating the end time of the current interval
            check_interval[1] = max(check_interval[1], current_interval[1])
        else:
            # no overlaps
            result.append(current_interval)
    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged = merged_intervals(intervals)
print("Merged intervals:", merged)
