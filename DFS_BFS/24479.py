# 알고리즘 수업 - 깊이 우선 탐색 1

n, m, r = map(int, input().split())

array = []
for _ in range(m):
    array.append(list(map(int, input().split())))

visited = [0] * (n + 1)



def dfs(r):
    visited[r] = 1
    for i in array:
        if visited[i[1]] != 1:
            dfs(i[1])

dfs(r)
for i in range(1, len(visited)):
    if visited[i] == 1:
        print(i)
    else:
        print(0)