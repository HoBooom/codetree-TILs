n,m = map(int,input().split())

grid = [
    [[]for _ in range(n)] for _ in range(n)
]

for r in range(n):
    nums = list(map(int,input().split()))
    for c in range(n):
        grid[r][c].append(nums[c])

move_nums = list(map(int,input().split()))

def is_range(r,c):
    return 0<=r<n and 0<=c<n

def find_n(num):
    for r in range(n):
        for c in range(n):
            if num in grid[r][c]:
                return (r,c)
    return -1,-1

def move(num):
    cnt_r,cnt_c = find_n(num)
    if r == -1: return

    drs,dcs = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]

    max_val = -1
    max_r, max_c = -1, -1

    for dr, dc in zip(drs, dcs):
        nr, nc = cnt_r + dr, cnt_c + dc
        if is_range(nr, nc) and grid[nr][nc]:
            local_max = max(grid[nr][nc])
            if local_max > max_val:
                max_val = local_max
                max_r, max_c = nr, nc

    # 이동할 위치가 있을 때만 이동
    if max_r != -1:
        move_idx = -1
        for i in range(len(grid[cnt_r][cnt_c])):
            if grid[cnt_r][cnt_c][i] == num:
                move_idx = i + 1
                break
        move_list = grid[cnt_r][cnt_c][:move_idx]

        grid[max_r][max_c] = move_list + grid[max_r][max_c]
        grid[cnt_r][cnt_c] = grid[cnt_r][cnt_c][move_idx:]



for num in move_nums:
    move(num)

    # for g in grid:
    #     print(*g)
    # print()



for r in range(n):
    for c in range(n):
        if len(grid[r][c]) == 0:
            print("None")
        else:
            print(*grid[r][c])



