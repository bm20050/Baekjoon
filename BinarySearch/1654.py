# 랜선 자르기

k, n = map(int, input().split())
data = []

for _ in range(k):
    data.append(int(input()))
start = 1
end = max(data)

while start <= end:
    count = 0
    mid = (start + end) // 2

    for i in data:
        count += i // mid
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
