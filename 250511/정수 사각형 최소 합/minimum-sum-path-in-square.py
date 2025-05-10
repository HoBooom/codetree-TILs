n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

sum_board = [[0 for _ in range(n)] for _ in range(n)]


def initialize():
    sum_board[0][n - 1] = board[0][n - 1]
    for c in range(n-2,-1,-1):
        sum_board[0][c] = sum_board[0][c + 1] + board[0][c]
    for r in range(1,n):
        sum_board[r][n-1] = sum_board[r - 1][n - 1] + board[r][n - 1]

initialize()
#print(*sum_board, sep="\n")

for r in range(1,n):
    for c in range(n-2,-1,-1):
        sum_board[r][c] = min(sum_board[r - 1][c],sum_board[r][c + 1]) + board[r][c]

#print(*sum_board, sep="\n")
print(sum_board[n-1][0])
