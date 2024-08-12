n = int(input())

MAX_K = 100

board = [
    [0 for _ in range(2*MAX_K + 1)] for _ in range(2*MAX_K + 1)
]

for _ in range(n):
    x0,y0 = map(int,input().split())
    for x in range(x0,x0 + 8):
        for y in range(y0,y0 + 8):
            board[x][y] = 1

count = 0

for x in range(2*MAX_K + 1):
    for y in range(2*MAX_K + 1):
        if board[x][y] == 1:
            count += 1

print(count)