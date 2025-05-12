n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = board[0][0]

#1행 처리
for c in range(1,n):
    dp[0][c] = min(dp[0][c-1],board[0][c])

#1열 처리
for r in range(1,n):
    dp[r][0] = min(dp[r-1][0],board[r][0])

#나머지 처리
for r in range(1,n):
    for c in range(1,n):
        from_top = min(board[r][c],dp[r-1][c])
        from_left = min(board[r][c],dp[r][c-1])
        dp[r][c] = max(from_left,from_top)

print(dp[n-1][n-1])

