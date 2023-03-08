# 단어 정렬

import sys

n = int(sys.stdin.readline())

data = []
for _ in range(n):
    data.append(sys.stdin.readline().strip())
data = list(set(data))
data.sort(key=lambda x: (len(x), x))

for i in data:
    print(i)
