import sys
input = sys.stdin.readline

n_size = int(input())
num = list(map(int, input().split()))
dp = num.copy()

for i in range(n_size):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + num[i])

print(max(dp))
