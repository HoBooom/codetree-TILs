n,m = map(int,input().split())

board = [
    [0 for _ in range(n)] for _ in range(n)
]

drs = [1,0,-1,0]
dcs = [0,1,0,-1]

direct = 0

def is_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < m

cnt = 1
r,c = 0,0
board[r][c] = cnt

while cnt < n*m:
    nr,nc = r + drs[direct], c + dcs[direct]

    if is_range(nr,nc) and board[nr][nc] == 0:
        r,c = nr,nc
        cnt += 1
        board[r][c] = cnt   
    else:
        direct = (direct + 1) % 4

for i in range(n):
    for j in range(m):
        print(board[i][j],end = " ")
    print()