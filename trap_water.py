#Trapping rain water
n = int(input("Enter the number of elements: "))
height = []
print("Enter the heights: ")
for i in range(n):
    height.append(int(input()))
left = 0
right = n - 1
left_max = 0
right_max = 0
water = 0
while left < right:
    if height[left] < height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]
        left += 1
    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]
        right -= 1
print("Total trapped water: ", water)