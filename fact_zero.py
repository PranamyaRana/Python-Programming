#Factorial trailing zeros
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 5
    count += n
print("Number of trailing zeros: ", count)