from collections import deque
import sys

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

INT_MAX = sys.maxsize
ans = INT_MAX

# Please write your code here.
def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def select_k_block(k):
    block_pos = [(r,c) for r in range(n) for c in range(n) if grid[r][c] == 1]
    block_sets = []

    def choose(cnt_idx, cnt_set):
        if len(cnt_set) == k:
            block_sets.append(cnt_set[:])
            return 
        
        if cnt_idx >= len(block_pos):
            return
        
        cnt_set.append(block_pos[cnt_idx])
        choose(cnt_idx + 1, cnt_set)

        cnt_set.pop()
        choose(cnt_idx + 1, cnt_set)
    
    choose(0,[])
    return block_sets
    
block_sets = select_k_block(k)

def gogo(block_set):
    global r1,c1,r2,c2,n

    for (r,c) in block_set:
        grid[r][c] = 0
    
    dis = [
        [-1 for _ in range(n)] for _ in range(n)
    ]

    q = deque()
    q.append((r1,c1))
    dis[r1][c1] = 0

    drs,dcs = [0,1,0,-1],[1,0,-1,0]

    while q:
        cnt_r,cnt_c = q.pop()

        for dr,dc in zip(drs,dcs):
            nr,nc = cnt_r + dr, cnt_c + dc
            if is_range(nr,nc) and grid[nr][nc] != 1:
                if dis[nr][nc] == -1:
                    dis[nr][nc] = dis[cnt_r][cnt_c] + 1
                    q.appendleft((nr,nc))
                elif dis[nr][nc] > dis[cnt_r][cnt_c] + 1:
                    dis[nr][nc] = dis[cnt_r][cnt_c] + 1
                    q.appendleft((nr,nc))
    
    for (r,c) in block_set:
        grid[r][c] = 1
    
    return dis[r2][c2]

for blocks in block_sets:
    cnt_dis = gogo(blocks)
    if cnt_dis != -1:
        ans = min(cnt_dis, ans)

if ans == INT_MAX:
    print(-1)
else:
    print(ans)