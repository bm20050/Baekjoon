# 좌표 정렬하기

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: x[1])
data.sort(key=lambda x: x[0])

for i in range(n):
    print(data[i][0], data[i][1])
