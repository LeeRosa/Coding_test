import sys
input = sys.stdin.readline

n, k = map(int, input().split())
gachi = []
for _ in range(n):
    gachi.append(int(input()))
# [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1
for i in gachi:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
        
print(dp[k])
