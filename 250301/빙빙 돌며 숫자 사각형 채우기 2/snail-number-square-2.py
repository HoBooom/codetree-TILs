n, m = map(int, input().split())

# Write your code here!

board = [[0 for _ in range(m)] for _ in range(n)]



def is_range(r,c):
    if 0 <= r < n and 0<= c < m:
        return True
    return False

cnt_r,cnt_c = -1,0

dr,dc = [1,0,-1,0],[0,1,0,-1]
dir_num = 0

cnt_num = 1
while cnt_num <= n*m:
    nr,nc = cnt_r + dr[dir_num],cnt_c + dc[dir_num]
    if is_range(nr,nc) and board[nr][nc] == 0:
        board[nr][nc] = cnt_num
        cnt_num += 1
        cnt_r,cnt_c = nr,nc
    else:
        dir_num = (dir_num + 1) % 4
        

for _,r in enumerate(board):
    for _,c in enumerate(r):
        print(c,end = " ")
    print()
        
        

