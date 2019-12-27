N = int(input())
input_nums = [int(x) for x in input().split()]
max_num = max(input_nums)
sieve = [True] * (max_num + 1)

sieve[1] = False
for num in range(2, max_num + 1):
    is_prime = sieve[num]
    if is_prime:
        for i in range(num * num, max_num + 1, num):
            sieve[i] = False
answer = 0
for input_num in input_nums:
    is_prime = sieve[input_num]
    if is_prime:
        answer += 1

print(answer)        

