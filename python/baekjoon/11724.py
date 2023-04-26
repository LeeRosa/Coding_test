import sys
from collections import deque
input = sys.stdin.readline


def graph(gansun, start, visit):
    need_visit = deque()
    need_visit.append(start)
    node = None

    while(need_visit):
        node = need_visit.pop()
        if visit[node] is False:
            visit[node] = True
            need_visit.extend(gansun[node])
    return visit, node


j_num, g_num = map(int, input().split())

gansun = dict()
for i in range(j_num):
    gansun[i] = []

for i in range(g_num):
    u, v = map(int, input().split())
    gansun[u-1].append(v-1)
    gansun[v-1].append(u-1)

visit = [False] * j_num
cnt = 0

for i in range(j_num):
    if not visit[i]:
        cnt += 1
        visit, node = graph(gansun, i, visit)

print(cnt)

#### 양방향이므로 u, v 넣어주고 v, u도 넣어주기!! 그리고 하나 혼자 있는 노드도 개수 세야한다.
#### dfs, bfs 구현 방법 익혀두기 
