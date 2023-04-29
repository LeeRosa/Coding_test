import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(m_map, x, y, m, n, visited, connect):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if visited[nx][ny] == False and m_map[nx][ny] == 0:
                connect += 1
                connect = dfs(m_map, nx, ny, m, n, visited, connect)

    return connect
    

m, n, k = map(int, input().split())

monun = [[0] * n for i in range(m)]
visited = [[False] * n for i in range(m)]
rect = []

for i in range(k):
    rect.append(list(map(int, input().split())))

for rec in rect:
    for x in range(rec[1], rec[3]):
        for y in range(rec[0], rec[2]):
            monun[x][y] = 1


cnt = 0
connect_num = []
for i in range(m):
    for j in range(n):
        if visited[i][j] == False and monun[i][j] == 0:
            connect = 1
            connect = dfs(monun, i, j, m, n, visited, connect)
            cnt += 1
            connect_num.append(connect)

print(cnt)
connect_num.sort()
for i in connect_num:
        print(i, end=' ')
