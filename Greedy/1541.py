# 잃어버린 괄호

s = input().split('-')

array = []
for i in range(len(s)):
    if '+' in s[i]:
        x = s[i].split('+')
        x = map(int, x)
        array.append(sum(x))
    else:
        array.append(int(s[i]))
result = array[0]
for i in range(1, len(array)):
    result -= array[i]

print(result)