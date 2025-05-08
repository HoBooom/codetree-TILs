n = int(input())

dp = [0] * 1001

dp[1] = 2
dp[2] = 7

for i in range(3,n + 1):
    dp[i] = (2 * dp[i - 1]) + (4 * dp[i - 2])

print(dp[n] % 1000000007)