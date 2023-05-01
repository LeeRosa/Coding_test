import sys
input = sys.stdin.readline

N = int(input())

stack = []
for i in range(N):
    commend = list(map(str, input().split()))
    com = commend[0]
    if com == 'push':
        stack.append(commend[1])
    elif com == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif com == 'size':
        print(len(stack))
    elif com == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif com == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)


