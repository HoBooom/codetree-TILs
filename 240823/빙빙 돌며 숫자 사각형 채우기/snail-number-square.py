n,m = map(int,input().split())

board = [
    [0 for _ in range(m)] for _ in range(n)
]

r = 0
c = -1

drs = [0,1,0,-1]
dcs = [1,0,-1,0]

direct = 0
cnt = 0

def is_range(r,c):
    return 0<=r and r < n and 0<=c and c<m

while True:
    nr,nc = r + drs[direct], c + dcs[direct]
    if is_range(nr,nc) and board[nr][nc] == 0:
        cnt += 1
        board[nr][nc] = cnt  
        if cnt == n*m:
            break
        r,c=nr,nc
    elif is_range(nr,nc) == False or board[nr][nc] != 0:
        direct = (direct + 1) % 4
    
    #print(i,cnt)
    

for i,v in enumerate(board):
    for index,value in enumerate(v):
        print(value,end=" ")
    print()