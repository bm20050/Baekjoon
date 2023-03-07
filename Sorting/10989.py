# 수 정렬하기 3

import sys

n = int(sys.stdin.readline())

count = [0] * (10001)

for i in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
