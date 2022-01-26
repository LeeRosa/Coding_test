import sys
input = sys.stdin.readline

T = int(input())
str = []

for i in range(T):
    str.append(input().strip())

def Palindrome(str, depth):
    queue = list(str)
    cnt = 0
    global flag
    flag = 0
    for j in range(int(len(str) / 2)):
        if flag == 1:
            if queue[j + 1] == queue[-(j + 1)]:
                cnt += 1
        elif flag == 2:
            if queue[j] == queue[-(j + 2)]:
                cnt += 1
        elif queue[j] == queue[-(j + 1)]:
            cnt += 1
        elif flag == 0:
            if j + 1 == len(str)-j:
                if queue[j + 2] == queue[-(j + 1)] or queue[j] == queue[-(j + 3)]:
                    flag = 1
                    cnt += 1
            else:
                if queue[j + 1] == queue[-(j + 1)]:
                    flag = 1
                    cnt += 1
                elif queue[j] == queue[-(j + 2)]:
                    flag = 2
                    cnt += 1

    if cnt == int(len(str)/2):
        if flag == 1 or flag == 2:
            return 1
        else:
            return 0
    else:
        if depth == 0:
            if Palindrome(str[::-1], 1) == 1:
                return 1
            return 2

for z in range(T):
    flag = 0
    print(Palindrome(str[z], 0))
