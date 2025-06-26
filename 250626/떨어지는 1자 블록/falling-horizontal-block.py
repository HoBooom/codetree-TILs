n,m,k = map(int,input().split())
k -= 1

grid = [list(map(int,input().split())) for _ in range(n)]

def check(r):
    for c in range(k,k + m):
        if grid[r][c] != 0:
            return False
    return True

def fall():
    clear = False
    for r in range(n):
        if not check(r):
            for i in range(m):
                grid[r - 1][k + i] = 1
            clear = True
            break
    if not clear:
        for i in range(m):
            grid[n - 1][k + i] = 1
        

def print_grid():
    for r in grid:
        print(*r)

fall()
print_grid()

