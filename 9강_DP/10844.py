N = int(input())
d = [[0] * 10 for _ in range(N+1)]
d[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2, N+1):
    for j in range(10):
        if j-1 >= 0:
            d[i][j-1] += d[i-1][j]
        if j+1 <= 9:
            d[i][j+1] += d[i-1][j]
print(sum(d[N]) % 1000000000)
"""
1   10
    12
2   21
    23
3   32
    34
4   43
    45
5   54
    56
6   65
    67
7   76
    78
8   87
    89
9   98
"""