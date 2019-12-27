N = int(input())
A = sorted([int(x) for x in input().split()])
M = int(input())
targets = [int(x) for x in input().split()]

def search(target, start=0, end=len(A)-1):
    if start > end:
        return 0
    mid = (start + end) // 2
    if A[mid] < target:
        start = mid + 1
    elif A[mid] > target:
        end = mid - 1
    else:
        return 1
    return search(target, start, end)

for target in targets:
    result = search(target)
    print(result)