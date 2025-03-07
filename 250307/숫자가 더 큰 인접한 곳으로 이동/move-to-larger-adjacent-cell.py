n, r, c = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dr,dc = [-1,1,0,0],[0,0,-1,1]

r,c = r - 1,c - 1

def is_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

print(board[r][c], end = " ")
while True:
    is_ok = False
    for dir_num in range(4):
        nr,nc = r + dr[dir_num], c + dc[dir_num]
        if is_range(nr,nc):
            if board[nr][nc] > board[r][c]:
                print(board[nr][nc], end=" ")
                r,c = nr,nc
                is_ok = True
        if is_ok:
            break 
    if is_ok == False:
        break