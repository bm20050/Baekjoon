# DFS와 BFS

from collections import deque

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * len(graph)
visited2 = [False] * len(graph)
dfsResult = []
bfsResult = []

for i in graph:
    i.sort()


def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


def bfs(x):
    q = deque([x])
    visited2[x] = True
    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not visited2[i]:
                q.append(i)
                visited2[i] = True


dfs(start)
print()
bfs(start)
