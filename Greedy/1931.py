# 회의실 배정

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort(key=lambda x: x[0])
array.sort(key=lambda x: x[1])

count = 0
start = 0
for i in array:
    if start <= i[0]:
        count += 1
        start = i[1]

print(count)
