from collections import deque
import sys

INT_MAX = sys.maxsize

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ans_grid = [
    [-1 for _ in range(n)] for _ in range(n)
]

pos_of_safe = [(r,c) for r in range(n) for c in range(n) if grid[r][c] == 3]

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def move(r,c):
    temp_grid = [
        [0 for _ in range(n)] for _ in range(n)
    ]

    drs,dcs = [0, 1, 0, -1],[1, 0, -1, 0]

    temp_min = INT_MAX

    q = deque()
    q.appendleft((r,c))

    while q:
        cnt_r,cnt_c = q.pop()

        for dr,dc in zip(drs,dcs):
            nr,nc = cnt_r + dr, cnt_c + dc
            if is_range(nr,nc) and grid[nr][nc] != 1:
                if temp_grid[nr][nc] == 0:
                    temp_grid[nr][nc] = temp_grid[cnt_r][cnt_c] + 1
                    q.appendleft((nr,nc))
                elif temp_grid[nr][nc] > temp_grid[cnt_r][cnt_c] + 1:
                    temp_grid[nr][nc] = temp_grid[cnt_r][cnt_c] + 1
                    q.appendleft((nr,nc))
    
    for (r,c) in pos_of_safe:
        if temp_grid[r][c] != 0:
            temp_min = min(temp_min, temp_grid[r][c])
    
    # print("=" *  20)
    # print(*temp_grid, sep='\n')
    if temp_min == INT_MAX:
        return -1
    return temp_min

for r in range(n):
    for c in range(n):
        if grid[r][c] == 2:
            ans_grid[r][c] = move(r,c)
            # print(ans_grid[r][c])
        else:
            ans_grid[r][c] = 0

for low in ans_grid:
    print(*low)



    


