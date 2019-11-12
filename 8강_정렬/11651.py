import sys
read = lambda: sys.stdin.readline()
N = int(read())
points = []
for _ in range(N):
    x, y = [int(k) for k in read().split()]
    points.append((y,x))

points.sort()
for point in points:
    print(point[1], point[0])