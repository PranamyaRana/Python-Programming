#3 sum
n = int(input("Enter the number of elements: "))
nums = []
print("Enter the elements: ")
for i in range(n):
    nums.append(int(input()))
nums.sort()
result = []
for i in range(n - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    left = i + 1
    right = n - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == 0:
            result.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1
print("Triplets with sum 0: ")
print(result)