import sys
read = lambda: sys.stdin.readline()
N = int(read())

time_table = []
max_time = 0
for _ in range(N):
    start, end = read().split()
    schedule = int(end), int(start)
    time_table.append(schedule)
    max_time = max(max_time, int(start))

time_table.sort()
time = 0
result = []
for schedule in time_table:
    if time <= schedule[1]:
        result.append(schedule)
        time = schedule[0]
        
print(len(result))