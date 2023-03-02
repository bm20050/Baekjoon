# 바이러스

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * len(graph)

def dfs(x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


dfs(1)

print(visited.count(True) - 1)