n = int(input())

board = [
    list(map(int,input().split())) for _ in range(n)
]

dxs = [1,0,-1, 0]
dys = [0,1, 0,-1]

def is_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def check(x,y):
    cnt = 0
    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy
        if is_range(nx,ny) and board[nx][ny] == 1:
            cnt += 1
    return cnt

count =0 
for i in range(n):
    for j in range(n):
        if check(i,j) >= 3:
            count += 1
print(count)