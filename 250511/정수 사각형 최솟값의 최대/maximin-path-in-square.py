n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

#print(*sum_board, sep="\n")
for r in range(n):
    for c in range(n):
        board[r][c] = min(max(board[r-1][c],board[r][c-1]),board[r][c])

print(board[n-1][n-1])