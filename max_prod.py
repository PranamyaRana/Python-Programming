#Maximum product subarray
n = int(input("Enter number of elements: "))
nums = []
print("Enter the elements: ")
for i in range(n):
    nums.append(int(input()))
max_prod = nums[0]
min_prod = nums[0]
result = nums[0]
for i in range(1, n):
    if nums[i] < 0:
        max_prod, min_prod = min_prod, max_prod
    if nums[i] > max_prod * nums[i]:
        max_prod = nums[i]
    else:
        max_prod = max_prod * nums[i]
    if nums[i] < min_prod * nums[i]:
        min_prod = nums[i]
    else:
        min_prod = min_prod * nums[i]
    if max_prod > result:
        result = max_prod
print("Maximum product subarray: ", result)