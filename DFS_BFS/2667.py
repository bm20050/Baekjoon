# 단지번호붙이기

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input())))

c = []
count = 0


def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if data[x][y] == 1:
        data[x][y] = 2
        count += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)


for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            dfs(i, j)
            c.append(count)
            count = 0

c.sort()
print(len(c))
for i in c:
    print(i)
