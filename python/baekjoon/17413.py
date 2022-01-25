import sys
from collections import deque
input = sys.stdin.readline

str = list(input().strip())
result = []
queue = deque()
flag = 0

for i in range(len(str)):
    if str[i] == ' ':
        while queue:
            result.append(queue.pop())
        result.append(str[i])
        
    elif str[i] == '<':
        while queue:
            result.append(queue.pop())
        flag = 1
        result.append(str[i])
        
    elif flag == 1 and str[i] == '>':
        flag = 0
        result.append(str[i])
        
    elif flag == 1:
        result.append(str[i])
        
    elif flag == 0:
        queue.append(str[i])

while queue:
    result.append(queue.pop())
print(''.join(result))
