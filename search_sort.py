#Search in rotated sorted array
n = int(input("Enter the number of elements: "))
nums = []
print("Enter the elements: ")
for i in range(n):
    nums.append(int(input()))
target = int(input("Enter the target element: "))
low = 0
high = n - 1
found_index = -1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        found_index = mid
        break
    if nums[low] <= nums[mid]:
        if nums[low] <= target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if nums[mid] < target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
print("Index of target: ", found_index)