n,m = map(int,input().split())

MAX_NUM = n * n

board = [list(map(int,input().split())) for _ in range(n)]

def turn(board):
    for i in range(1, MAX_NUM + 1):
        is_change = False
        for r in range(n):
            for c in range(n):
                if board[r][c] == i:
                    # print(i)
                    change(r,c)
                    is_change = True
                    break
            if is_change:
                break

def is_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

def change(r,c):
    dr,dc = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
    temp = 0
    t_r,t_c = -1,-1
    for dir_num in range(8):
        nr,nc = r + dr[dir_num], c + dc[dir_num]
        if is_range(nr,nc):
            if temp < board[nr][nc]:
                temp = board[nr][nc]
                t_r,t_c = nr,nc
    board[t_r][t_c],board[r][c] = board[r][c],board[t_r][t_c]
    # for r in range(n):
    #     print(*board[r])
    # print()

for i in range(m):
    turn(board)

for r in range(n):
    print(*board[r])
            
