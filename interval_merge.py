#Merge Intervals
n = int(input("Enter the number of intervals: "))
intervals = []
print("Enter the intervasl (start and end): ")
for i in range(n):
    start = int(input("Start: "))
    end = int(input("End: "))
    intervals.append([start, end])
intervals.sort()
merged = []
for interval in intervals:
    if not merged:
        merged.append(interval)
    else:
        last = merged[-1]
        if interval[0] <= last[1]:
            if interval[1] > last[1]:
                last[1] = interval[1]
        else:
            merged.append(interval)
print("Merged intervals: ")
print(merged)