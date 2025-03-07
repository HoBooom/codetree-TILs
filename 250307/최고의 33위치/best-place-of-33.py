n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

total_count = 0

for i in range(n - 2):
    for j in range(n - 2):
        count = 0
        count += sum(board[i][j:j+3])
        count += sum(board[i + 1][j:j+3])
        count += sum(board[i + 2][j:j+3])
        total_count = max(total_count,count)
print(total_count)
        
