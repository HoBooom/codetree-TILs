n = int(input())

board = [[0 for _ in range(230)] for _ in range(230)] 

def color(x1,y1,x2,y2):
    for x in range(x1,x2):
        for y in range(y1,y2):
            board[y][x] += 1



for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    color(x1,y1,x2,y2)

ans = 0

for y in range(230):
    for x in range(230):
        if board[y][x] >= 1:
            ans += 1

print(ans)
