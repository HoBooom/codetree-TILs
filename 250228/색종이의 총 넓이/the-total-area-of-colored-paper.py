n = int(input())

board = [[0 for _ in range(230)] for _ in range(230)]

def color(x,y):
    for i in range(x,x + 8):
        for j in range(y,y + 8):
            board[j][i] += 1

for _ in range(n):
    x,y = map(int,input().split())
    x,y = x + 100, y + 100
    color(x,y)

ans = 0

for i in range(230):
    for j in range(230):
        if board[i][j] >= 1:
            ans += 1
print(ans)
