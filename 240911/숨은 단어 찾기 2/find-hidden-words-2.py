n,m = map(int,input().split())

board = [
    list(input()) for _ in range(n)
]

def is_range(r,c):
    return 0<=r<n and 0<=c<m

drs = [-1,-1,-1,0,1,1,1,0]
dcs = [-1,0,1,1,1,0,-1,-1]

count =0


for r in range(n):
    for c in range(m):
        if board[r][c] != 'L':
            continue
        elif board[r][c] == 'L':
            for dr,dc in zip(drs,dcs):
                nr,nc = r + dr,c+dc
                if is_range(nr,nc) and board[nr][nc] == 'E':
                    new_nr,new_nc = nr + dr, nc + dc
                    if is_range(new_nr,new_nc) and board[new_nr][new_nc] =='E':
                        count += 1

print(count)