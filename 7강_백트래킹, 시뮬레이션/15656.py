import sys
read = lambda: sys.stdin.readline()
numbers = []
N, M = [int(x) for x in read().split()]
numbers = sorted([int(x) for x in read().split()])
answer = [None for _ in range(M)]


def solution(depth=0):
    if depth == M:
        print(*answer)
        return
    for index in range(N):
        answer[depth] = numbers[index]
        solution(depth + 1)
        
solution()

# 두배 가량 더 빠른 버전
# import sys
# read = lambda: sys.stdin.readline()
# numbers = []
# N, M = [int(x) for x in read().split()]
# numbers = sorted([int(x) for x in read().split()])


# def solution(depth, answer):
#     if depth == M:
#         print(answer)
#         return
#     for index in range(N):
#         solution(depth + 1, answer + str(numbers[index]) + " ")

# solution(0, '')
