from collections import deque

def bfs(maze, visited, row, col):

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    start = [0, 0]
    goal = [row-1, col-1]
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v == goal:
            print(visited[v[0]][v[1]]+1)
            break
        for j in range(4):
            if 0 <= v[0] + dy[j] < row and 0 <= v[1] + dx[j] < col and visited[v[0] + dy[j]][v[1] + dx[j]] == 0 and maze[v[0] + dy[j]][v[1] + dx[j]] == '1':
                queue.append([v[0] + dy[j], v[1] + dx[j]])
                visited[v[0]+dy[j]][v[1]+dx[j]] = visited[v[0]][v[1]] + 1

row, col = map(int, input().split())
maze = []
for i in range(row):
    maze.append(input())
visited = [[0]*col for _ in range(row)]

bfs(maze, visited, row, col)
