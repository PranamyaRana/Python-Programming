#Check if pair with the given sum exists in array
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the numbers: ")
for i in range(n):
    arr.append(int(input()))
target = int(input("Enter the sum you want to find: "))
found = False
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            print("Indices: ", i, j)
            found = True
            break
    if found:
        break
if not found:
    print("No pair exists.")