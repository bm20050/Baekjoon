# 동전 0

n, k = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

count = 0
for i in array:
    if k >= i:
        count += k // i
        k %= i

print(count)
