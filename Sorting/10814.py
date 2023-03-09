# 나이순 정렬

import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(list(map(str, sys.stdin.readline().split())))

data.sort(key=lambda x: int(x[0]))

for i in data:
    print(i[0], i[1])
