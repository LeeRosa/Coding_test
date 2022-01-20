from collections import deque

def bfs(tomato, visited, ik_to, row, col):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()

    for t in range(len(ik_to)):
        queue.append(ik_to[t])

    while queue:
        v = queue.popleft()
        for r in range(4):
            if 0 <= v[0]+dy[r] < row and 0 <= v[1]+dx[r] < col and tomato[v[0]+dy[r]][v[1]+dx[r]] == '0' and visited[v[0]+dy[r]][v[1]+dx[r]] == 0:
                queue.append([v[0]+dy[r],v[1]+dx[r]])
                visited[v[0]+dy[r]][v[1]+dx[r]] = visited[v[0]][v[1]] + 1

    if min(map(min, visited)) == 0:
        print('-1')
    else:
        print(max(map(max, visited))-1)

col, row = map(int, input().split())
tomato = []
ik_to = []
visited = [[0]*col for _ in range(row)]

for i in range(row):
    tomato.append(input().split())

for j in range(row):
    for k in range(col):
        if tomato[j][k] == '1':
            ik_to.append([j, k])
            visited[j][k] = 1
        if tomato[j][k] == '-1':
            visited[j][k] = 1

bfs(tomato, visited, ik_to, row, col)
