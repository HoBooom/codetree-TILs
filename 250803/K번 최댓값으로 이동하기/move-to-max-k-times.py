from collections import deque

n, k = map(int,input().split())

grid  = [
    list(map(int,input().split())) for _ in range(n)
]

cnt_r, cnt_c = map(int,input().split())
cnt_r, cnt_c = cnt_r - 1, cnt_c - 1

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def move(cnt_r,cnt_c):
    can_go = [
        [False for _ in range(n)] for _ in range(n)
    ]

    queue = deque()

    queue.appendleft((cnt_r,cnt_c))
    can_go[cnt_r][cnt_c] = True

    drs, dcs = [0,1,0,-1],[1,0,-1,0]
    cnt_max = 0

    while queue:
        c_r, c_c = queue.pop()

        for dr, dc in zip(drs,dcs):
            nr,nc = c_r + dr, c_c + dc
            if is_range(nr,nc) and grid[nr][nc] < grid[cnt_r][cnt_c] and not can_go[nr][nc]:
                queue.appendleft((nr,nc))
                can_go[nr][nc] = True
                cnt_max = max(cnt_max, grid[nr][nc])
    
    if cnt_max == 0:
        return cnt_r,cnt_c
    
    for r in range(n):
        for c in range(n):
            if grid[r][c] == cnt_max:
                return r,c
    
        

for _ in range(k):
    nr,nc = move(cnt_r,cnt_c)
    if (nr,nc) == (cnt_r,cnt_c):
        break
    cnt_r,cnt_c = nr,nc

print(cnt_r + 1,cnt_c + 1)