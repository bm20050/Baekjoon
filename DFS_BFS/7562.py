# 나이트의 이동

from collections import deque

n = int(input())

next = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]


def bfs(a, b, l):
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        if x == n and y == m:
            return graph[x][y]
        for i in next:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


for _ in range(n):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    a, b = map(int, input().split())
    n, m = map(int, input().split())

    print(bfs(a, b, l))
