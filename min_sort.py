#Find minimum in rotated sorted array
n = int(input("Enter the number of elements: "))
nums = []
print("Enter the elements: ")
for i in range(n):
    nums.append(int(input()))
low = 0
high = n - 1
while low < high:
    mid = (low + high) // 2
    if nums[mid] > nums[high]:
        low = mid + 1
    else:
        high = mid
print("Minimum element: ", nums[low])