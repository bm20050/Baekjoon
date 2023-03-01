# ATM

n = int(input())
array = list(map(int, input().split()))

array.sort()

sum = 0
temp = 0
for i in array:
    temp += i
    sum += temp

print(sum)