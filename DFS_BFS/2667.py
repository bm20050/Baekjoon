# 단지번호붙이기

from collections import deque
n = int(input())

data = []
for _ in range(n):
    data.append(list(input()))

temp = [[0] * n for _ in range(n)]
print(temp)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque([x, y])
    temp[x][y] = 1
    for i in range(n):
        for j in range(n):
            if data[i][j] == '1' and temp[i][j] != 1:
                temp[i][j] = 1
                q.append(i, j)
                bfs(i, j)


