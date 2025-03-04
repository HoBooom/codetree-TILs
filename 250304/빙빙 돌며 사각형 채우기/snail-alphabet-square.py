n,m = map(int,input().split())

board = [['0' for _ in range(m)] for _ in range(n)]

dr,dc = [0,1,0,-1],[1,0,-1,0]
dir_num = 0
cnt_r,cnt_c = (0,-1)
cnt_alpha = ord('A')
cnt_num = 0

def is_range(r,c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False

while True:
    nr,nc = cnt_r + dr[dir_num],cnt_c + dc[dir_num]
    if cnt_num >= n*m:
        break
    if is_range(nr,nc) and board[nr][nc] == '0':
        cnt_num += 1
        board[nr][nc] = chr(cnt_alpha)
        if cnt_alpha == 90:
            cnt_alpha = 65
        else:
            cnt_alpha += 1
        cnt_r,cnt_c = nr,nc
    else:
        dir_num = (dir_num + 1) % 4

for r in range(n):
    for c in range(m):
        print(board[r][c],end = " ")
    print()




    
