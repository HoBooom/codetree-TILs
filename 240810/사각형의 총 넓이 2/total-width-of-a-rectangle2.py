n = int(input())

MAX_K = 100

board = [
    [0 for _ in range(2*MAX_K + 1)] for _ in range(2*MAX_K + 1)
]


for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            board[x + MAX_K][y + MAX_K] = 1

area = 0

for i in range(2*MAX_K + 1):
    for j in range(2* MAX_K + 1):
        if board[i][j] == 1:
            area += 1


print(area)