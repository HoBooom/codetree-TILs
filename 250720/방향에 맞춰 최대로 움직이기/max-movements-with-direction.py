n = int(input())

grid_n = [
    list(map(int,input().split())) for _ in range(n)
]

grid_dir = [
    list(map(int,input().split())) for _ in range(n)
]

cnt_r,cnt_c = map(int,input().split())
cnt_r, cnt_c = cnt_r - 1, cnt_c - 1

ans = 0

#moves = [(cnt_r,cnt_c)]

drs,dcs = [0,-1,-1,0,1,1,1,0,-1],[0,0,1,1,1,0,-1,-1,-1]

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def check_and_move(cnt_r, cnt_c, count):
    global ans 
    dir_n = grid_dir[cnt_r][cnt_c]
    ori_n = grid_n[cnt_r][cnt_c]
    for i in range(n):
        nr, nc = cnt_r + drs[dir_n], cnt_c + dcs[dir_n]
        if is_range(nr,nc):
            if grid_n[nr][nc] > ori_n:
                count += 1
                #moves.append((nr,nc))
                check_and_move(nr, nc, count)
                count -= 1
            cnt_r,cnt_c = nr,nc
                
    #print(*moves)
    ans = max(count, ans)
    return

check_and_move(cnt_r,cnt_c,0)
print(ans)

                



