import sys
input = sys.stdin.readline

def dfs(c_dict, start, visited):

    visited[start] = True
    need_visit = c_dict[start]

    for i in need_visit:
        if visited[i] is False:
            visited[i] = True
            need_visit.extend(c_dict[i])


c_num = int(input())
connect_num = int(input())

connect = dict()
for i in range(c_num):
    connect[i+1] = []

for i in range(connect_num):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

visited = [False] * (c_num+1)
dfs(connect, 1, visited)
print(visited.count(True)-1)

##### deque로 푼 버전
'''
import sys
from collections import deque
input = sys.stdin.readline

def dfs(c_dict, start, visited):
    visited[start] = True
    need_visit = deque()
    need_visit.extend(c_dict[start])

    while need_visit:
        node = need_visit.pop()
        if visited[node] is False:
            visited[node] = True
            need_visit.extend(c_dict[node])

c_num = int(input())
connect_num = int(input())

connect = dict()
for i in range(c_num):
    connect[i+1] = []

for i in range(connect_num):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

visited = [False] * (c_num+1)
dfs(connect, 1, visited)
print(visited.count(True)-1)
'''

### 이번 문제는 bfs로 간단히 
### 해결할 수 있는 문제였다!
### list 말고 deque로 하는 것이 더 좋다고 함!
