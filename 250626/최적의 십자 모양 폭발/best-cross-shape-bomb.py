n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def boom(r,c,temp_grid):
    boom_size = temp_grid[r][c]

    drs,dcs = [-1,0,1,0],[0,1,0,-1]
    for dr,dc in zip(drs,dcs):
        for b in range(boom_size):
            nr,nc = r + (dr * b), c + (dc * b)
            if is_range(nr,nc):
                temp_grid[nr][nc] = 0
    
    return temp_grid

def reset(temp_grid):
    reset_grid = [[0 for _ in range(n)] for _ in range(n)]

    for c in range(n):
        next_r = n - 1
        for r in reversed(range(n)):
            if temp_grid[r][c] != 0:
                reset_grid[next_r][c] = temp_grid[r][c]
                next_r -= 1

    
    return reset_grid


def check(cnt_grid):
    count = 0
    for r in range(n):
        for c in range(n - 1):
            if cnt_grid[r][c] != 0 and cnt_grid[r][c] == cnt_grid[r][c + 1]:
                count += 1
    
    for r in range(n - 1):
        for c in range(n):
            if cnt_grid[r][c] != 0 and cnt_grid[r][c] == cnt_grid[r + 1][c]:
                count += 1
    
    return count

def print_grid(cnt_grid):
    for r in cnt_grid:
        print(*r)
    print()
ans = 0

for r in range(n):
    for c in range(n):
        temp_grid = [[grid[r][c] for r in range(n)] for c in range(n)]
        #print("-------------")
        
        temp_grid = boom(r,c,temp_grid)
        temp_grid = reset(temp_grid)

        #print_grid(temp_grid)
        ans = max(ans, check(temp_grid))
        #print(ans, check(temp_grid))
        

print(ans)

