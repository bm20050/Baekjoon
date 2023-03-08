# 소트인사이드

n = input()
array = []
for i in n:
    array.append(i)
array.sort(reverse=True)
print(''.join(array))
