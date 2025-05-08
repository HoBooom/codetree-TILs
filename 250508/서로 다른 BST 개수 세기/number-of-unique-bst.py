n = int(input())

dp = [0] * 20

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,n + 1): #점근적으로 dp_n 계산
    for j in range(1, i + 1): #j를 루트로 하기로 생각
        dp[i] += (dp[j - 1] * dp[i - j])

print(dp[n])
