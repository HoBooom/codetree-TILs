n = int(input())
MOD = 1000000007

dp = [0] * 1001

dp[0] = 1
dp[1] = 2
dp[2] = 7
#dp[3] = 22

for i in range(2,n + 1):
    dp[i] = (2 * dp[i - 1]) + (3 * dp[i - 2]) % MOD
    for j in range(i - 3, -1, -1):
        dp[i] = (dp[i] + dp[j] * 2) % MOD

print(dp[n])