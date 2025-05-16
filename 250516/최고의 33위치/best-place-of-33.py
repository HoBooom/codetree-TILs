n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

ans = 0

for r in range(n-2):
    for c in range(n-2):
        count = 0
        count += sum(board[r][c:c+3])
        count += sum(board[r+1][c:c+3])
        count += sum(board[r+2][c:c+3])
        ans = max(ans,count)

print(ans)