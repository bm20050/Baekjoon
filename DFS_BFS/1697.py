# 숨바꼭질

from collections import deque

n, k = map(int, input().split())
next = [1, -1, 0]
visited = [0] * 100001


def bfs(a):
    queue = deque([a])
    while queue:
        x = queue.popleft()
        visited[a] = 1
        next[2] = x
        for i in next:
            if i + x < 0 or i + x > 100000:
                continue
            if visited[i + x] == 0:
                visited[i + x] = visited[x] + 1
                queue.append(i + x)
            if i + x == k:
                return visited[k] - 1


print(bfs(n))
