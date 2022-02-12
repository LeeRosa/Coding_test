import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stone = list(map(int, input().split()))

dp = [0]*N
dp[0] = 1
for i in range(N-1):
    if dp[i] == 1:
        for j in range(i+1, N):
            if dp[j] == 0 and K >= (j-i)*(1+abs(stone[i]-stone[j])):
                dp[j] = 1
if dp[N-1] == 1:
    print('YES')
else:
    print('NO')
