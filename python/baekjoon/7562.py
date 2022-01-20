from collections import deque

def bfs(start, goal, visited, c_size, result):
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    queue = deque([start])
    visited[start[0]][start[1]] = 1

    while queue:
        v = queue.popleft()
        if v == goal:
            result.append(visited[v[0]][v[1]]-1)
            break
        for i in range(8):
            if 0 <= v[0]+dx[i] < c_size and 0 <= v[1]+dy[i] < c_size and visited[v[0]+dx[i]][v[1]+dy[i]] == 0:
                queue.append([v[0]+dx[i], v[1]+dy[i]])
                visited[v[0]+dx[i]][v[1]+dy[i]] = visited[v[0]][v[1]] + 1

test_num = int(input())
chess_size = []
result = []

for t in range(test_num):
    chess_size.append(int(input()))
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    start = [sx, sy]
    goal = [gx, gy]
    visited = [[0]*chess_size[t] for _ in range(chess_size[t])]
    bfs(start, goal, visited, chess_size[t], result)

for r in range(test_num):
    print(result[r])
