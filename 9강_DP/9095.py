"""
d[0] = 1
d[1] = sum { d[0] }        // d[-1] , d[-2]     : 1     = 1
d[2] = sum { d[1], d[0] }  //  d[-1]            : 1 + 1 = 2
d[3] = sum { d[2], d[1], d[0] }                 : 2 + 1 + 1 = 4 
d[4] = sum { d[3], d[2], d[1] }                 : 4 + 2 + 1 = 7
d[5] ...
"""
import sys
read = lambda: sys.stdin.readline()

T = int(read()) 
list_n = []
for _ in range(T):
    n = int(read())
    list_n.append(n)
max_n = max(list_n)


def solve(n):
    d = [0] * (n + 1)
    d[0] = 1
    for i in range(1, n + 1):
        value = 0
        for count in range(1, 4):
            temp = i - count
            if temp < 0:
                break
            value += d[temp]
        d[i] = value
    return d

d = solve(max_n)
for n in list_n:
    print(d[n])


