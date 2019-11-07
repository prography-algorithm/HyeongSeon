import sys
RIGHT = "D"
apples = set()
timestamps = []
read = lambda: sys.stdin.readline()
N = int(read())
K = int(read())
for _ in range(K):
    line, row = (int(x) for x in read().split())
    apples.add((row, line))
L = int(read())
for _ in range(L):
    second, rotation = [x for x in read().split()]
    timestamp = (int(second), rotation)
    timestamps.append(timestamp)

def solution():
    count = 0
    snake = Snake()
    for timestamp in timestamps:
        for _ in range(count, timestamp[0]):
            snake.move()
            count += 1
            if snake.is_conflict:
                return count
        direction = timestamp[1]
        snake.rotate(direction)
    while not snake.is_conflict:
        snake.move()
        count += 1
    return count

"""
뱀은 꿈 틀 하고 움직인다.
꿈: 일단 한칸 움직임
틀: 몸을 움추림, 사과를 먹으면 안 움추림.
"""
class Snake:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def __init__(self):
        self._locations = [(1, 1)]
        self.is_conflict = False
        self._direction_order = 0
    @property
    def head(self):
        return self._locations[-1]
    
    @property
    def direction(self):
        return self.DIRECTIONS[self._direction_order]

    def check_conflict(self):
        return self._check_confilct_with_map() or self._check_conflict_with_self()
    
    def _check_confilct_with_map(self):
        line = self.head[0]
        row = self.head[1] 
        return line > N or line < 1 or row > N or row < 1

    def _check_conflict_with_self(self):
        return self._locations.count(self.head) == 2
    
    def rotate(self, direction):
        if direction == RIGHT:
            self._direction_order += 1
        else:
            self._direction_order -= 1
        self._direction_order %= 4

    def move(self):
        self._move_ggoom()
        if self.check_conflict():
            self.is_conflict = True
        self._move_ttle()

    def _move_ggoom(self):
        head = self.head
        self._locations.append((head[0] + self.direction[0], head[1] + self.direction[1]))

    def _move_ttle(self):
        if self.head not in apples:
            self._locations.pop(0)
        else:
            apples.remove(self.head)


print(solution())
