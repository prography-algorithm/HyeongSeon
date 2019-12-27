N = int(input())
nums = [int(x) for x in input().split()]

start = 0
end = N - 1
temp = nums[start] + nums[end]

optimum_start = start
optimum_end = end
optimum_temp = temp

while start < end:
    if temp == 0:
        break
    elif temp < 0:
        start += 1
    else:
        end -= 1
    if start == end:
        break
    temp = nums[start] + nums[end]
    if abs(optimum_temp) > abs(temp):
        optimum_temp = temp
        optimum_start, optimum_end = start, end

print(nums[optimum_start], nums[optimum_end])
"""
6
-11 -3 2 3 5 7
5
-5 -4 -3 -2 -1
6
-7 -5 -3 -2 3 11
"""