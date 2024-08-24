n,m = map(int,input().split())

MAX_K = 100

board = [
    [0 for _ in range(2*MAX_K + 1)] for _ in range(2*MAX_K + 1)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def is_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def check(x,y):
    temp = 0
    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx,y + dy
        if board[nx][ny] == 1:
            temp += 1
    if temp == 3:
        return True
    return False

for _ in range(m):
    r,c = map(int,input().split())
    r,c = r + MAX_K, c + MAX_K
    board[r][c] = 1
    if check(r,c):
        print(1)
    else:
        print(0)