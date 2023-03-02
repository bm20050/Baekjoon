# 주유소

n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
minPrice = 1000000000
for i in range(len(length)):
    if price[i] < minPrice:
        minPrice = price[i]
    result += minPrice * length[i]

print(result)