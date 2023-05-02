##적록색약
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(art, x, y, N, visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and art[nx][ny] == art[x][y] and visited[nx][ny] == False:
            dfs(art, nx, ny, N, visited)


N = int(input())

art = []
for i in range(N):
    art.append(list(map(str, input())))

art_gr = [['']*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if art[i][j] == 'G':
            art_gr[i][j] = 'R'
        else:
            art_gr[i][j] = art[i][j]

visited = [[False] * N for i in range(N)]
visited_gr = [[False] * N for i in range(N)]
cnt = 0
cnt_gr = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(art, i, j, N, visited)
            cnt += 1

        if visited_gr[i][j] == False:
            dfs(art_gr, i, j, N, visited_gr)
            cnt_gr += 1

print(cnt, cnt_gr)
