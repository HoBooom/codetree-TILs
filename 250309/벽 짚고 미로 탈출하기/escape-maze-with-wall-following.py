n = int(input())

cnt_r,cnt_c = map(int,input().split())
cnt_r -= 1
cnt_c -= 1

board = [list(input()) for _ in range(n)]

#벽을 만났을때
dr,dc = [0,-1,0,1],[1,0,-1,0]

#벽이 없을때
#dr2,dc2 = [0,1,0,-1],[1,0,-1,0]

dir_num = 0
start_r,start_c = cnt_r,cnt_c
time = 0

def is_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

def is_right_block(r,c):
    b_r,b_c = r + dr[(dir_num - 1) % 4], c + dc[(dir_num - 1) % 4]
    if is_range(b_r,b_c) and board[b_r][b_c] == '#':
        return True
    return False

while True:
    if time != 0 and (cnt_r,cnt_c) == (start_r,start_c):
        time = -1
        break

    nr,nc = cnt_r + dr[dir_num],cnt_c + dc[dir_num]
    
    if not is_range(nr,nc):
        time += 1
        break
    else: # 만약 nr,nc가 보드 안에 있다면
        #만약 앞의 놈이 벽이면
        if board[nr][nc] == '#':
            dir_num = (dir_num + 1) % 4
        else:
            if is_right_block(nr,nc):
                cnt_r,cnt_c = nr,nc
                time += 1
            else:
                cnt_r,cnt_c = nr,nc
                time += 1
                dir_num = (dir_num - 1) % 4

print(time)


