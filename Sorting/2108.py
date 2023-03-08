# 통계학

from collections import Counter
import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()

print(round(sum(data) / n))
print(data[len(data) // 2])
x = Counter(data).most_common()
x.sort(key=lambda y: y[1], reverse=True)
if len(x) > 1 and x[0][1] == x[1][1]:
    print(x[1][0])
else:
    print(x[0][0])
print(max(data) - min(data))
