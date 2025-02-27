
board = [[0 for _ in range(2030)] for _ in range(2030)]

def color(x1,y1,x2,y2):
    for x in range(x1,x2 + 1):
        for y in range(y1,y2 + 1):
            board[y][x] += 1

def erase(x1,y1,x2,y2):
    for x in range(x1,x2 + 1):
        for y in range(y1,y2 + 1):
            board[y][x] -= 1


for i in range(2):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1 + 1000,y1 + 1000,x2 + 1000,y2 + 1000
    if i == 0:
        color(x1,y1,x2,y2)
    else:
        erase(x1,y1,x2,y2)


max_x = 0
min_x = 2030
max_y = 0
min_y = 2030

for x in range(2030):
    for y in range(2030):
        if board[y][x] >= 1:
            max_x = max(x,max_x)
            min_x = min(x,min_x)
            max_y = max(y,max_y)
            min_y = min(y,min_y)

#print(max_x,max_y,min_x,min_y)
ans = (abs(max_x - min_x)  * abs(max_y - min_y))
print(ans)

