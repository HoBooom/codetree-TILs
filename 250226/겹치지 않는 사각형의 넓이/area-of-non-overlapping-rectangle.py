board = [[0 for _ in range(2010)] for _ in range(2010)]

def color(x1,y1,x2,y2):
    for x in range(x1,x2):
        for y in range(y1,y2):
            board[y][x] += 1

def erase(x1,y1,x2,y2):
    for x in range(x1,x2):
        for y in range(y1,y2):
            board[y][x] -= 1

for i in range(3):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000
    if i == 2:
        erase(x1,y1,x2,y2)
    else:
        color(x1,y1,x2,y2)

ans = 0
for y in range(2010):
    for x in range(2010):
        if board[y][x] == 1:
            ans += 1

print(ans)