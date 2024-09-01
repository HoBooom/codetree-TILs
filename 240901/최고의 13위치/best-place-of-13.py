n = int(input())


board = [
    list(map(int,input().split())) for _ in range(n)
]

max_count = 0

for i in range(n):
    for j in range(n - 2):
        temp = board[i][j] + board[i][j + 1] + board[i][j + 2]
        max_count = max(max_count,temp)

print(max_count)