# 나무 자르기

import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(data)

while start <= end:
    mid = (start + end) // 2
    length = 0
    for i in data:
        if mid < i:
            length += i - mid

    if length >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)