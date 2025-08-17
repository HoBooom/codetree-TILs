n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def is_range(r,c):
    return 0 <= r < n and 0 <= c < m

distance = [
    [0 for _ in range(m)] for _ in range(n)
]

q = deque()

cnt_r,cnt_c = 0,0

q.append((cnt_r,cnt_c))

drs,dcs = [0,1,0,-1],[1,0,-1,0]

while q:
    cnt_r, cnt_c = q.pop()

    for dr,dc in zip(drs,dcs):
        nr,nc = cnt_r + dr, cnt_c + dc
        if is_range(nr,nc) and grid[nr][nc] == 1:
            if distance[nr][nc] == 0:
                distance[nr][nc] = distance[cnt_r][cnt_c] + 1
                q.appendleft((nr,nc))
            elif distance[nr][nc] > distance[cnt_r][cnt_c] + 1:
                distance[nr][nc] = distance[cnt_r][cnt_c] + 1
                q.appendleft((nr,nc))

if distance[n - 1][m - 1] == 0:
    print(-1)
else:
    print(distance[n - 1][m - 1])




