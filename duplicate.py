#Find the duplicate number
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))
found = False
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            print("The duplicate number is: ", arr[i])
            found = True
    if found:
        break
if not found:
    print("No duplicate number exists")