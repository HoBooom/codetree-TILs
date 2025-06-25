n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

def boom(n,r,c):
    drs,dcs = [-1,0,1,0],[0,1,0,-1]

    for dr,dc in zip(drs,dcs):
        for i in range(n):
            nr,nc = r + (dr * i), c + (dc * i)
            if is_range(nr,nc):
                grid[nr][nc] = 0


def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def reset():
    for c in range(n):
        temp_c = []
        for r in reversed(range(n)):
            if grid[r][c] != 0:
                temp_c.append(grid[r][c])
        len_c = len(temp_c)

        for i in range(len_c):
            grid[n - i - 1][c] = temp_c[i]

        for j in range(n - len_c):
            grid[j][c] = 0

        
for _ in range(m):
    c = int(input())
    c -= 1
    for r in range(n):
        if grid[r][c] != 0:
            boom(grid[r][c], r, c)
            reset()
            break
    
for row in grid:
    print(*row)


