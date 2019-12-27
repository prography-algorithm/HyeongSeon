N = int(input())
A = sorted([int(x) for x in input().split()])
M = int(input())
targets = [int(x) for x in input().split()]

def get_lower_idx(target, length):
    start = 0
    end = length
    while start < end:
        mid = (start + end) // 2
        if A[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

def get_upper_idx(target, length):
    start = 0
    end = length
    while start < end:
        mid = (start + end) // 2
        if A[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start

answer = []
for target in targets:
    upper_idx = get_upper_idx(target, N)
    lower_idx = get_lower_idx(target, N)
    answer.append(upper_idx - lower_idx)

print(*answer)

# 이전 코드

# N = int(input())
# A = sorted([int(x) for x in input().split()])
# M = int(input())
# targets = [int(x) for x in input().split()]

# def get_upper_idx(target, start=0, end=len(A)-1, is_target_found=False):
#     if start == end and is_target_found:
#         return start
#     if start >= end:
#         return -1
        
#     mid = (start + end + 1) // 2
#     if A[mid] < target:
#         start = mid + 1
#     elif A[mid] > target:
#         end = mid - 1
#     else:
#         is_target_found = True
#         return get_upper_idx(target, mid, end, is_target_found)
#     return get_upper_idx(target, start, end, is_target_found)

# def get_lower_idx(target, start=0, end=len(A)-1, is_target_found=False):
#     if start == end and is_target_found:
#         return start
#     if start > end:
#         return -1

#     mid = (start + end) // 2
#     if A[mid] < target:
#         start = mid + 1
#     elif A[mid] > target:
#         end = mid - 1
#     else:
#         is_target_found = True
#         return get_lower_idx(target, start, mid, is_target_found)
#     return get_lower_idx(target, start, end, is_target_found)

# answer = []
# for target in targets:
#     lower_idx = get_lower_idx(target)
#     if lower_idx == -1:
#         answer.append(0)
#         continue
#     upper_idx = get_upper_idx(target)
#     if len(A) == 1:
#         upper_idx = 0
#     answer.append(upper_idx - lower_idx + 1)

# print(*answer)