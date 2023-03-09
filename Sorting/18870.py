#  좌표 압축

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
ndata = sorted(set(data))
d = dict()
for i in range(len(ndata)):
    if ndata[i] not in d:
        d[ndata[i]] = i

for i in data:
    print(d[i], end=' ')
