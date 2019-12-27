"""
    15 28 19
16  1 16 16
    1 16 31
    16 44
    16 35
17  2 17 17
18  3 18 18
19  4 19 19
20  5 20 1
    5 20 35
    20 48
    1 20
21  6 21 2
22  7 22 3
28  13 28 9
29  14 1 10
    14 29
    1 29
    10 29
"""

E, S, M = [int(x) for x in input().split()]
# 15 28 19
year = 1
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0
"""
year % 15 = E
year % 28 = S
year % 19 = M
"""
while not (year % 15 == E and year % 28 == S and year % 19 == M):
    year += 1
print(year)