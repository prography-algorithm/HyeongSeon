# pypy3
import sys
sys.setrecursionlimit(100000)

def read():
    return sys.stdin.readline()


N, L, R = map(int, read().split())
countries = [[0] * N for _ in range(N)]

for y in range(N):
    populations = [int(x) for x in read().split()]
    for x in range(N):
        countries[x][y] = populations[x]


def is_union(a, b):
    value = abs(a - b)
    return value <= R and value >= L


def migrate(union):
    population_sum = 0
    for country_location in union:
        x, y = country_location
        population_sum += countries[x][y]
    avarage = population_sum // len(union)
    for country_location in union:
        x, y = country_location
        countries[x][y] = avarage
    return avarage


def unite_dfs(x, y, visited, union):
    visited[x][y] = True
    union.append((x, y))
    for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if is_union(countries[x][y], countries[nx][ny]) and not visited[nx][ny]:
            unite_dfs(nx, ny, visited, union)


def solution(count = 0):
    visited = [[False] * N for _ in range(N)]
    unions = []
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                union = []
                unite_dfs(x, y, visited, union)
                if len(union) > 1:
                    unions.append(union)
    if not unions:
        return count
    else:
        count += 1
    for union in unions:
        migrate(union)
    return solution(count)

print(solution())
