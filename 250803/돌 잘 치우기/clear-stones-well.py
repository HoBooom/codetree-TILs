from collections import deque
import itertools

n, k, m = map(int,input().split())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

points = [
    tuple(map(int,input().split())) for _ in range(k)
]

choose = [
    [False for _ in range(n)] for _ in range(n)
]

ans = 0

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def check():
    visited = [
        [False for _ in range(n)] for _ in range(n)
    ]
    drs,dcs = [0,1,0,-1],[1,0,-1,0]
    count = 0
    q = deque()
    for point in points:
        start_r,start_c = point
        start_c -= 1
        start_r -= 1
        if not visited[start_r][start_c]:
            q.append((start_r,start_c))
            visited[start_r][start_c] = True
            count += 1

            while q:
                cnt_r,cnt_c = q.pop()

                for dr,dc in zip(drs,dcs):
                    nr,nc = cnt_r + dr, cnt_c + dc
                    if is_range(nr,nc) and not visited[nr][nc] and grid[nr][nc] == 0:
                        q.appendleft((nr,nc))
                        visited[nr][nc] = True
                        count += 1
    return count

def make_grid():
    global ans, m, n

    is_zero = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 1] 
    combinations = list(itertools.combinations(is_zero,m))

    for combination in combinations:
        for combo in combination:
            temp_r,temp_c = combo
            grid[temp_r][temp_c] = 0
        
        cnt_check = check()
        ans = max(ans,cnt_check)

        for combo in combination:
            temp_r,temp_c = combo
            grid[temp_r][temp_c] = 1

make_grid()
print(ans)





    

    

