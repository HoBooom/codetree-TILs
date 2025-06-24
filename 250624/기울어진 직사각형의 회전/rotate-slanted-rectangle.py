n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

r,c,m1,m2,m3,m4,dir_n = map(int,input().split())
r,c = r - 1,c - 1

def shift_0():
    temp = grid[r][c]

    cnt_r,cnt_c = r,c
    for _ in range(m4):
        grid[cnt_r][cnt_c] = grid[cnt_r - 1][cnt_c - 1]
        cnt_r,cnt_c = cnt_r - 1,cnt_c - 1
    
    for _ in range(m3):
        grid[cnt_r][cnt_c] = grid[cnt_r - 1][cnt_c + 1]
        cnt_r,cnt_c = cnt_r - 1,cnt_c + 1
    
    for _ in range(m2):
        grid[cnt_r][cnt_c] = grid[cnt_r + 1][cnt_c + 1]
        cnt_r,cnt_c = cnt_r + 1,cnt_c + 1
    
    for _ in range(m1):
        grid[cnt_r][cnt_c] = grid[cnt_r + 1][cnt_c - 1]
        cnt_r,cnt_c = cnt_r + 1,cnt_c - 1
    
    grid[cnt_r - 1][cnt_c + 1] = temp

def shift_1():
    temp = grid[r][c]

    cnt_r,cnt_c = r,c
    for _ in range(m1):
        grid[cnt_r][cnt_c] = grid[cnt_r - 1][cnt_c + 1]
        cnt_r,cnt_c = cnt_r - 1,cnt_c + 1
    
    for _ in range(m2):
        grid[cnt_r][cnt_c] = grid[cnt_r - 1][cnt_c - 1]
        cnt_r,cnt_c = cnt_r - 1,cnt_c - 1
    
    for _ in range(m3):
        grid[cnt_r][cnt_c] = grid[cnt_r + 1][cnt_c - 1]
        cnt_r,cnt_c = cnt_r + 1,cnt_c - 1
    
    for _ in range(m4):
        grid[cnt_r][cnt_c] = grid[cnt_r + 1][cnt_c + 1]
        cnt_r,cnt_c = cnt_r + 1,cnt_c + 1
    
    grid[cnt_r - 1][cnt_c - 1] = temp

if dir_n == 0:
    shift_0()
else:
    shift_1()

for row in grid:
    print(*row)