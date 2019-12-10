N = int(input())
d = [[0]*2 for _ in range(N+1)]
d[1][1] = 1

for i in range(2, N+1):
    d[i][0] += sum(d[i-1])
    d[i][1] += d[i-1][0]

print(sum(d[N]))
