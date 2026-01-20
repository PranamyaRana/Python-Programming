#Container with most water
n = int(input("Enter the number of elements: "))
height = []
print("Enter the heights: ")
for i in range(n):
    height.append(int(input()))
left = 0
right = n - 1
max_water = 0
while left < right:
    width = right - left
    if height[left] < height[right]:
        current_water = height[left] * width
        left += 1
    else:
        current_water = height[right] * width
        right -= 1
    if current_water > max_water:
        max_water = current_water
print("Maximum water that can be stored: ", max_water)