# 알고리즘 수업 - 깊이 우선 탐색 2

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m, r = map(int, input().split())

array = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    array[u].append(v)
    array[v].append(u)

visited = [0] * (n + 1)

count = 1


def dfs(x):
    global count
    if visited[x] == 1:
        return
    visited[x] = count
    array[x].sort(reverse=True)
    for i in array[x]:
        if visited[i] == 0:
            count += 1
            dfs(i)


dfs(r)

for i in range(1, n + 1):
    print(visited[i])
