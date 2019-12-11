"""
4
-1
2
1
3  6
양수는 큰 순서대로, 1이랑은 묶으면 안됨
음수는 절댓값이 큰 순서대로
-1 0 1 2 4
"""
import sys
read = lambda: sys.stdin.readline()

N = int(read())
minus_nums = []
plus_nums = []
for _ in range(N):
    num = int(read())
    if num <= 0:
        minus_nums.append(num)
    else:
        plus_nums.append(num)        
minus_nums.sort()
plus_nums.sort(reverse=True)

result = 0

minus_temp = None
for num in minus_nums:
    if minus_temp is None:
        minus_temp = num
    else:
        result += minus_temp * num
        minus_temp = None
if minus_temp is not None:
    result += minus_temp

plus_temp = None
for num in plus_nums:
    if plus_temp is None:
        plus_temp = num
    elif num == 1:
        result += num
    else:
        result += plus_temp * num
        plus_temp = None
if plus_temp is not None:
    result += plus_temp

print(result)