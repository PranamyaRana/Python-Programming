#Insert Interval
n = int(input("Enter the number of intervals: "))
intervals = []
print("Enter the intervals (start and end): ")
for i in range(n):
    start = int(input("Start: "))
    end = int(input("End: "))
    intervals.append([start, end])
new_start = int(input("Enter the new interval start: "))
new_end = int(input("Enter the new interval end: "))
result = []
i = 0
while i < n and intervals[i][1] < new_start:
    result.append(intervals[i])
    i += 1
while i < n and intervals[i][0] < new_end:
    new_start = min(new_start, intervals[i][0])
    new_end = max(new_end, intervals[i][1])
    i += 1
result.append([new_start, new_end])
while i < n:
    result.append(intervals[i])
    i += 1
print("Intervals after insertion: ")
print(result)