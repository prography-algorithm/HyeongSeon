"""
d[0] = {None: 1, 
        left: 0, 
        right: 0}
d[1] = {0: d[1 -1][None] + d[1 -1][left] + d[1 -1][right],  1 
        left: d[1 -1][right] + d[1 -1][None],               1
        right: d[1 -1][left] + d[1 -1][None]}               1
d[2] =  3
        2
        2
d[2] 
"""
# 메모리 초과
LEFT = 'l'
RIGHT = 'r'
N = int(input())
d = [None] * (N + 1)
d[0] = {None: 1,
        LEFT: 0,
        RIGHT: 0, }

for i in range(1, N + 1):
    d[i] = {None: d[i - 1][None]+ d[i - 1][LEFT] + d[i - 1][RIGHT],
            LEFT: d[i - 1][RIGHT] + d[i - 1][None],
            RIGHT: d[i - 1][LEFT] + d[i - 1][None]}
answer = sum(d[N].values())
print(answer % 9901)

# 백준 통과
LEFT = 'l'
RIGHT = 'r'
N = int(input())
d = [None] * (N + 1)
d[0] = {None: 1,
        LEFT: 0,
        RIGHT: 0, }

for i in range(1, N + 1):
    d[i] = {None: d[i - 1][None] % 9901 + d[i - 1][LEFT] + d[i - 1][RIGHT],
            LEFT: d[i - 1][RIGHT] + d[i - 1][None] % 9901,
            RIGHT: d[i - 1][LEFT] + d[i - 1][None] % 9901}
answer = sum(d[N].values())
print(answer % 9901)
# 왜 for 문 안에서도 9901로 나눠줘야 하나?

# N = int(input())
# d = [None] * (N + 1)
# d[0] = (1, 0)

# for i in range(1, N + 1):
#     cache = d[i-1]
#     d[i] = (cache[0] + cache[1] * 2, cache[0] + cache[1])
# answer = d[N][0] + d[N][1] * 2
# print(answer % 9901)

# N = int(input())
# d = [None] * (N + 1)
# d[0] = (1, 0)

# for i in range(1, N + 1):
#     cache = d[i-1]
#     d[i] = ((cache[0] + cache[1] * 2) % 9901, (cache[0] + cache[1]) % 9901)
# answer = d[N][0] + d[N][1] * 2
# print(answer)
