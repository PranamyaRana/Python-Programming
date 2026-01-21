#Non-overlapping intervals
n = int(input("Enter the number of intervals: "))
intervals = []
print("Enter the intervals (start and end): ")
for i in range(n):
    start= int(input("Start: "))
    end = int(input("End: "))
    intervals.append([start, end])
intervals.sort(key=lambda x: x[1])
count_remove = 0
prev_end = intervals[0][1]
for i in range(1, n):
    if intervals[i][0] < prev_end:
        count_remove += 1
    else:
        prev_end = intervals[i][1]
print("Minimum number of intervals to remove: ", count_remove)