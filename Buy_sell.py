#Best time to buy and sell stocks
n = int(input("Enter the number of days: "))
prices = []
print("Enter stock prices: ")
for i in range(n):
    prices.append(int(input()))
max_profit = 0
for i in range(n):
    for j in range(i+1, n):
        profit = prices[j] - prices[i]
        if profit > max_profit:
            max_profit = profit
print("Maximum profit: ", max_profit)