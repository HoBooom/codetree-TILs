n,m = map(int,input().split())

board = [
    ['0' for _ in range(m)] for _ in range(n) 
]

drs = [0,1,0,-1]
dcs = [1,0,-1,0]

cnt = 'A'
check = 1
r,c = 0,0
direct = 0
board[r][c] = cnt

def is_range(r,c):
    return 0<=r<n and 0<=c<m

while check < n*m:
    nr,nc = r + drs[direct],c + dcs[direct]

    if is_range(nr,nc) and board[nr][nc] == '0':
        r,c = nr,nc
        if cnt == 'Z':
            cnt = 'A'
        else:
            cnt = chr(ord(cnt) + 1)
        board[r][c] = cnt
        check += 1
    else:
        direct = (direct + 1)%4

for i in range(n):
    for j in range(m):
        print(board[i][j],end=" ")
    print()