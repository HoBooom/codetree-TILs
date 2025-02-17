import sys

MAXSIZE = sys.maxsize

n = int(input())

board = [tuple(map(int,input().split())) for _ in range(n)]

def f(board):
    x_list = []
    y_list = []
    for _,(x,y) in enumerate(board):
        x_list.append(x)
        y_list.append(y)
    x0,x1 = min(x_list),max(x_list)
    y0,y1 = min(y_list),max(y_list)
    x = abs(x1 - x0)
    y = abs(y1 - y0)
    return x * y

ans = MAXSIZE

for i in range(n):
    tboard = []
    temp = 0
    for j in range(n):
        if i == j:
            continue
        tboard.append(board[j])
    temp = f(tboard)
    if temp < ans:
        ans = temp

print(ans)

    


        
