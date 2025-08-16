from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
time = 0
last_iceberg = -1

def is_clear():
    if 1 not in grid:
        return True
    return False

def is_range(r,c):
    return 0 <= r < n and 0 <= c < m

def check():
    water_grid = [
        [False for _ in range(m) for _ in range(n)]
    ]
    melt_grid = [
        [False for _ in range(m) for _ in range(n)]
    ]
    melted_ice = 0

    drs, dcs = [0, 1, 0, -1],[1, 0, -1, 0]

    dq = deque()

    dq.appendleft((0,0))

    while dq:
        cnt_r,cnt_c = dq.pop()

        for (dr, dc) in zip(drs, dcs):
            nr,nc = cnt_r + dr, cnt_c + dc
            if is_range(nr,nc) and grid[nr][nc] == 0 and not water_grid[nr][nc]:
                dq.appendleft((nr,nc))
            if grid[nr][nc] == 1:
                melt_grid[nr][nc] = True
    
    for r in range(n):
        for c in range(m):
            if melt_grid[r][c]:
                grid[r][c] = 0
    
    

while True:
    if not is_clear():
        check()
        time += 1
    else:
        break
    

        
        
