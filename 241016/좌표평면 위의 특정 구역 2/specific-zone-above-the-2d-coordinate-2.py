import sys

MAX_INT = sys.maxsize

n = int(input())

board = [
    tuple(map(int,input().split())) for i in range(n)
]

ans = MAX_INT

for i in range(n):
    max_x = max_y = -1
    min_x = min_y = 40001

    for k in range(n):
        if k == i:
            continue
        
        max_x = max(board[k][0],max_x)
        min_x = min(board[k][0],min_x)

        max_y = max(board[k][1],max_y)
        min_y = min(board[k][1],min_y)
    area = abs(max_x - min_x) * abs(max_y - min_y)
    ans = min(ans,area)

print(ans)