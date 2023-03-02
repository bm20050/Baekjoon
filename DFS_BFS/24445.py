# 알고리즘 수업 - 너비 우선 탐색 2

from collections import deque
import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())

array = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    array[u].append(v)
    array[v].append(u)

visited = [0] * (n + 1)
c = 1


def bfs(x):
    global c
    q = deque([r])
    visited[x] = c
    c += 1
    while q:
        a = q.popleft()
        array[a].sort(reverse=True)
        for i in array[a]:
            if visited[i] == 0:
                visited[i] = c
                c += 1
                q.append(i)


bfs(r)

for i in range(1, len(visited)):
    print(visited[i])
