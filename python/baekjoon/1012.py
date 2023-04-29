import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(b_map, x, y, w, h, visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[x][y] = True    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if visited[nx][ny] == False and b_map[nx][ny] == 1:
                dfs(b_map, nx, ny, w, h, visited)
    return visited

test_num = int(input())
j_cnt = []
for i in range(test_num):
    w, h, bachu_num = map(int, input().split())

    bachu_map = [[0] * h for j in range(w)]

    for j in range(bachu_num):
        x, y = map(int, input().split())
        bachu_map[x][y] = 1

    visited = [[False] * h for j in range(w)]
    cnt = 0

    for k in range(w):
        for l in range(h):
            if bachu_map[k][l] == 1 and visited[k][l] == False:
                visited = dfs(bachu_map, k, l, w, h, visited)
                cnt += 1
                
    j_cnt.append(cnt)

for j in range(len(j_cnt)):
    print(j_cnt[j])
    
#### 재귀 깊이 제한 걸어줘야함 !!! 
#### sys.setrecursionlimit(10 ** 6) 기억해두자
