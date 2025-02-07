n = int(input())
grid = [[0] * n for _ in range(n)]

# Write your code here!
#1,1, 2,2
cnt_num = 1

cnt_r,cnt_c = n // 2, n // 2
grid[cnt_r][cnt_c] = cnt_num
cnt_num += 1

def is_range(r,c):
    if 0<= r < n and 0<= c<n:
        return True
    return False


change = 1

dr,dc = [0,-1,0,1],[1,0,-1,0]
dir_num = 0

while True:
    for _ in range(2):
        for _ in range(change):
            nr,nc = cnt_r + dr[dir_num],cnt_c + dc[dir_num]
            if is_range(nr,nc) and grid[nr][nc] == 0:
                grid[nr][nc] = cnt_num
                cnt_num += 1
                cnt_r,cnt_c = nr,nc
        dir_num = (dir_num + 1) % 4
    change += 1
    if cnt_num > n**2:
        break

for _,r in enumerate(grid):
    for _,c in enumerate(r):
        print(c,end = " ")
    print()


