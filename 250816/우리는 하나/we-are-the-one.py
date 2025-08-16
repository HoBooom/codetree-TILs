from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# Please write your code here.
# choose
def find_combination(grid, k):
    idx_set = [(r,c) for r in range(n) for c in range(n)]

    combo_set = []

    def backtrack(cnt_idx, cnt_combo):
        if len(cnt_combo) == k:
            combo_set.append(cnt_combo[:])
            return

        if cnt_idx >= len(idx_set):
            return
        
        cnt_combo.append(idx_set[cnt_idx])
        backtrack(cnt_idx + 1, cnt_combo)

        cnt_combo.pop()
        backtrack(cnt_idx + 1, cnt_combo)
    
    backtrack(0,[])
    return combo_set

# main
def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def check_city(combo):
    global u,d
    city_count = 0
    city = [
        [False for _ in range(n)] for _ in range(n)
    ]
    dq = deque()
    for (r,c) in combo:
        dq.appendleft((r,c))
        city[r][c] = True
        city_count += 1
    
    drs,dcs = [0, 1, 0, -1],[1, 0, -1, 0]
    

    while dq:
        cnt_r, cnt_c = dq.pop()

        for dr, dc in zip(drs, dcs):
            nr,nc = cnt_r + dr, cnt_c + dc
            if is_range(nr,nc) and not city[nr][nc]:
                if u <= abs(grid[nr][nc] - grid[cnt_r][cnt_c]) <= d:
                    dq.appendleft((nr,nc))
                    city[nr][nc] = True
                    city_count += 1
    return city_count
        
    


combination_set = find_combination(grid, k)

for combo in combination_set:
    cnt_count = check_city(combo)
    #print(combo, cnt_count)
    ans = max(ans, cnt_count)

print(ans)

