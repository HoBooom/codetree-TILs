n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

sum_board = [[0 for _ in range(n)] for _ in range(n)]

def initialize():
    sum_board[0][0] = board[0][0]
    for i in range(1,n):
        sum_board[i][0] = board[i][0] + sum_board[i - 1][0]
    for i in range(1,n):
        sum_board[0][i] = board[0][i] + sum_board[0][i - 1]

initialize()

#print(*sum_board, sep="\n")
for r in range(1,n):
    for c in range(1,n):
        sum_board[r][c] = max(sum_board[r-1][c],sum_board[r][c-1]) + board[r][c]

print(sum_board[n-1][n-1])