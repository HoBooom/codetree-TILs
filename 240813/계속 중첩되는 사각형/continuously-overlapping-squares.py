n = int(input())

MAX_K = 100

board = [
    [0 for _ in range(2*MAX_K + 1)] for _ in range(2*MAX_K + 1)
]

for i in range(n):
    if i % 2 == 0: #red
        x1,y1,x2,y2 = map(int,input().split())
        for x in range(x1,x2):
            for y in range(y1,y2):
                board[x][y] = 1
    else:
        x1,y1,x2,y2 = map(int,input().split())
        for x in range(x1,x2):
            for y in range(y1,y2):
                board[x][y] = 2

count = 0

for x in range(2*MAX_K + 1):
    for y in range(2*MAX_K + 1):
        if board[x][y] == 2:
            count += 1

print(count)