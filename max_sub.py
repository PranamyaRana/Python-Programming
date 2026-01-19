#Maximum subarray
n = int(input("Enter the number of elements: "))
num = []
print("Enter the elements: ")
for i in range(n):
    num.append(int(input()))
max_sum = num[0]
current_sum = num[0]
for i in range(1, n):
    if current_sum + num[i] > num[i]:
        current_sum = current_sum + num[i]
    else:
        current_sum = num[i]
    if current_sum > max_sum:
        max_sum = current_sum
print("Maximum subarray sum: ", max_sum)