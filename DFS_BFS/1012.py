# 유기농 배추

from collections import deque

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, row, col):
    queue = deque()
    data[x][y] = 2
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if data[nx][ny] == 0 or data[nx][ny] == 2:
                continue
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                queue.append((nx, ny))


answer = []
for _ in range(t):
    n, m, k = map(int, input().split())
    data = [[0] * (m) for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        data[a][b] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                count += 1
                bfs(i, j, n, m)
    answer.append(count)

for i in answer:
    print(i)
