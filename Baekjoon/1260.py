import sys
from collections import deque
input = sys.stdin.readline

def dfs(gansun, start, visit_dfs):
    queue = deque()
    queue.extend(gansun[start])
    visit_dfs[start] = True
    print(start, end=' ')

    for i in queue:
        if visit_dfs[i] == False:
            dfs(gansun, i, visit_dfs)

def bfs(gansun, start, visit_bfs):
    queue = deque()
    queue.extend([start])
    visit_bfs[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in gansun[v]:
            if visit_bfs[i] == False:
                visit_bfs[i] = True
                queue.append(i)


N, M, V = map(int, input().split())

gansun = dict()
for i in range(N):
    gansun[i+1] = []

for i in range(M):
    u, v = map(int, input().split())
    gansun[u].append(v)
    gansun[v].append(u)
    
for i in range(N):
    gansun[i+1] = sorted(gansun[i+1])

visit_dfs = [False] * (N+1)
visit_bfs = [False] * (N+1)

dfs(gansun, V, visit_dfs)
print()
bfs(gansun, V, visit_bfs)
