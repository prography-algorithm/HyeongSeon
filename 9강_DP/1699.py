"""
d[1] : 1 = 1^2              1
d[2] : 2 = 1^2 + 1^2        2
d[3] : 3 = 1^2 + 1^2 + 1^2  3
d[4] : 4 = 2^2              1
d[5] : 5 = 2^2 + 1          2
d[6] : 6 = 2^2 + 1 + 1      3
d[7] : 7 = 2^2 + 1 + 1 + 1  4
d[8] : 8 = 2^2 + 2^2        2
d[9] : 9 = 3^2              1
d[10]: 10 = 3^2 + 1         2
d[11]: 11 = 3^2 + 1 + 1     3
d[12]: 12 = 2^2 + 2^2 + 2^2 3
        12 = 1 + 1 + 1 + 3^2 (4) 3보다 크니깐 무시
d[13]: 13 = 2^2 + 3^2
        13 = 3^2 + 2^2
hint:
d[i] <= d[i -1] + 1

"""
n = int(input())
d = [0] * (n + 1)

key = 2
for i in range(1, n + 1):
    if i == key * key:
        d[i] = 1
        key += 1
        continue
    temps = [d[i-1] + 1]
    for low_key in range(1, key):
        temps.append(d[i - low_key * low_key] + 1)
    d[i] = min(temps)

print(d[n])


