n = int(input())

board = [
    [0 for _ in range(n)] for _ in range(n)
]

center = n // 2
r,c = center,center

drs = [0,-1,0,1]
dcs = [1,0,-1,0]
direct = 0

cnt = 1
walk = 1

board[r][c] = cnt


def is_range(r,c):
    return 0<=r<n and 0<=c<n

check = 0
temp = 0
while cnt < n**2:
    if temp == walk:
        direct = (direct + 1) % 4
        temp = 0
        check += 1
        if check == 2:
            walk += 1
            check = 0
    
    nr,nc = r + drs[direct],c + dcs[direct]
    if is_range(nr,nc) and board[nr][nc] == 0:
        r,c = nr,nc
        cnt += 1
        board[r][c] = cnt
        temp += 1 

for i in range(n):
    for j in range(n):
        print(board[i][j],end = " ")
    print()