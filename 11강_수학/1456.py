A, B = [int(x) for x in input().split()]
answer = 0
max_num = min(B + 1, 10000001)
nums = [True] * (max_num)
for i in range(2, max_num):
    if not nums[i]:
        continue
    for j in range(i*i, max_num, i):
        nums[j] = False
    k = i * i
    while (k <= B):
        if A <= k:
            answer += 1
        k *= i

print(answer)


    