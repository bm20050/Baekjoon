# 스택
import sys

n = int(input())
stack = [0] * 10000
top = -1
for _ in range(n):
    s = sys.stdin.readline().strip()
    # print(s)
    if 'push' in s:
        top += 1
        s = s.split(' ')
        stack[top] = int(s[1])
    elif s == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif s == 'size':
        print(top + 1)
    elif s == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif s == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])

