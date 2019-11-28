import sys
read = lambda: sys.stdin.readline()

n = int(read())
wines = [None]
for _ in range(n):
    wine = int(read())
    wines.append(wine)

d = [[0] * 3 for _ in range(n + 1)]
d[1][1] = wines[1]
for i in range(2, n + 1):
    d[i][0] = max(d[i-1])
    d[i][1] = max(d[i-1][0], d[i-2][1], d[i-2][2]) + wines[i]
    d[i][2] = d[i-1][1] + wines[i]
    
print(max(d[n-1]))

# import sys
# read = lambda: sys.stdin.readline()

# n = int(read())
# wines = [None]
# for _ in range(n):
#     wine = int(read())
#     wines.append(wine)

# d = [[0] * 3 for _ in range(n + 1)]
# d[1][1] = wines[1]
# for i in range(2, n + 1):
#     d[i][1] = max(d[i-2][1], d[i-2][2]) + wines[i]
#     d[i][2] = d[i-1][1] + wines[i]
    
# print(max(max(d[n]), max(d[n-1])))
    
    