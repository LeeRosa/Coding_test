from collections import deque

row, col = map(int, input().split())
s_map = []
for i in range(row):
    s_map.append(input())

visited = [[[0]*2 for _ in range(col)] for __ in range(row)]

def bfs(s_map, row, col, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([0, 0, 1])
    goal = [row-1, col-1]
    visited[0][0][1] = 1

    while queue:
        v = queue.popleft()
        if [v[0], v[1]] == goal:
            return visited[v[0]][v[1]][v[2]]

        for r in range(4):
            y = v[0] + dy[r]
            x = v[1] + dx[r]
            if 0 <= y < row and 0 <= x < col:
                if s_map[y][x] == '0' and visited[y][x][v[2]] == 0:
                    queue.append([y, x, v[2]])
                    visited[y][x][v[2]] = visited[v[0]][v[1]][v[2]] + 1
                elif s_map[y][x] == '1' and v[2] == 1:
                    visited[y][x][0] = visited[v[0]][v[1]][v[2]] + 1
                    queue.append([y, x, 0])
    return -1

print(bfs(s_map, row, col, visited))
