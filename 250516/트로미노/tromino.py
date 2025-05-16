n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

dr,dc = [-1,0,1,0],[0,1,0,-1]


def is_range(r,c):
    return 0 <= r < n and 0 <= c < m

def check1(r,c):
    cnt_max = 0
    for dir_n in range(4):
        t1_r,t1_c = r + dr[dir_n], c + dc[dir_n]
        t2_r,t2_c = r + dr[(dir_n + 1) % 4], c + dc[(dir_n + 1) % 4]
        if is_range(t1_r,t1_c) and is_range(t2_r,t2_c):
            temp = (board[r][c]+board[t1_r][t1_c]+board[t2_r][t2_c])
            cnt_max = max(temp,cnt_max)
    return cnt_max

def check2(r,c):
    cnt_max = 0
    for dir_n in range(4):
        t1_r,t1_c = r + dr[dir_n], c + dc[dir_n]
        t2_r,t2_c = t1_r + dr[dir_n], t1_c + dc[dir_n]
        if is_range(t1_r,t1_c) and is_range(t2_r,t2_c):
            temp = (board[r][c]+board[t1_r][t1_c]+board[t2_r][t2_c])
            cnt_max = max(temp,cnt_max)
    return cnt_max

ans = 0

for r in range(n):
    for c in range(m):
        ans = max(check1(r,c),check2(r,c),ans)

print(ans)

            
    
    