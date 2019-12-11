import sys
read = lambda: sys.stdin.readline()

N, money = [int(x) for x in read().split()]
coins = []
for _ in range(N):
    coins.append(int(read()))

result = 0
for i in range(len(coins) - 1, -1, -1):
    coin = coins[i]
    if coin <= money:
        temp = money // coin
        result += temp
        money -= coin * temp

print(result)
