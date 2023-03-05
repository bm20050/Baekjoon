# 수 찾기

n = int(input())
aN = list(map(int, input().split()))
m = int(input())
aM = list(map(int, input().split()))

aN.sort()


def binary_search(x):
    first = 0
    last = n - 1

    while first <= last:
        mid = (first + last) // 2
        if aN[mid] < x:
            first = mid + 1
        elif aN[mid] > x:
            last = mid - 1
        else:
            return True
    return False


for i in aM:
    if binary_search(i):
        print(1)
    else:
        print(0)
