import sys

board = [
    list(map(int,input().split())) for _ in range(19)
]

def is_range(r,c):
    return 0<=r<19 and 0<=c<19

drs = [-1,-1,-1,0,1,1,1,0]
dcs = [-1,0,1,1,1,0,-1,-1]

for r in range(19):
    for c in range(19):
        if board[r][c] == 0:
            continue
        
        for dr,dc in zip(drs,dcs):

            cnt_count = 1
            cnt_row = r
            cnt_column = c

            while True:
                nr,nc = cnt_row +  dr, cnt_column + dc
                if not is_range(nr,nc):
                    break
                if board[nr][nc] != board[r][c]:
                    break
                cnt_count += 1
                cnt_row = nr
                cnt_column = nc
            
            if cnt_count == 5:
                print(board[r][c])
                print(r + 2*dr + 1,c + 2*dc + 1)
                sys.exit()

print(0)