#Product of array except itself
n = int(input("Enter the number of elements: "))
num = []
print("Enter the elements: ")
for i in range(n):
    num.append(int(input()))
answer = [1] * n
prefix = 1
for i in range(n):
    answer[i] = prefix
    prefix = prefix * num[i]
suffix = 1
for i in range(n-1, -1, -1):
    answer[i] = answer[i] * suffix
    suffix = suffix * num[i]
print("Result array: ", answer)