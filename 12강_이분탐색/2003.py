N, M = map(int, input().split())
nums = [int(x) for x in input().split()]

count = 0
left = 0
right = 0
temp = 0
while right < N:
    if temp < M:
        temp += nums[right]
        right += 1
    elif temp >= M:
        if temp == M:
            count += 1
        temp -= nums[left]
        left += 1
if temp == M:
    count += 1
print(count)