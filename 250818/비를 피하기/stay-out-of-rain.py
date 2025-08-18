from collections import deque

n,h,m = map(int,input().split())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

distance = [
    [-1 for _ in range(n)] for _ in range(n)
]

drs,dcs = [0,1,0,-1],[1,0,-1,0]

q = deque()

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

for r in range(n):
    for c in range(n):
        if grid[r][c] == 3:
            q.appendleft((r,c))
            distance[r][c] = 0

while q:
    cnt_r,cnt_c = q.pop()

    for dr,dc in zip(drs,dcs):
        nr,nc = cnt_r + dr, cnt_c + dc
        if is_range(nr,nc) and grid[nr][nc] != 1:
            if distance[nr][nc] == -1:
                distance[nr][nc] = distance[cnt_r][cnt_c] + 1
                q.appendleft((nr,nc))
            elif distance[nr][nc] > distance[cnt_r][cnt_c] + 1:
                distance[nr][nc] = distance[cnt_r][cnt_c] + 1
                q.appendleft((nr,nc))

ans_grid = [
    [0 for _ in range(n)] for _ in range(n)
]

for r in range(n):
    for c in range(n):
        if grid[r][c] == 2:
            ans_grid[r][c] = distance[r][c]

for low in ans_grid:
    print(*low)

