n,m,k = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

def reset():
    temp_grid = [[0 for _ in range(n)] for _ in range(n)]

    for c in range(n):
        next_r = n - 1
        for r in reversed(range(n)):
            if grid[r][c] != 0:
                temp_grid[next_r][c] = grid[r][c]
                next_r -= 1
    
    for r in range(n):
        for c in range(n):
            grid[r][c] = temp_grid[r][c]

def booom():
    #열 별로 폭탄이 터짐
    for c in range(n):
        cnt_count = 1
        start_r = 0
        for r in range(1,n):
            if grid[r][c] == grid[start_r][c]:
                cnt_count += 1
            else:
                if cnt_count >= m:
                    for i in range(cnt_count):
                        grid[start_r + i][c] = 0
                cnt_count = 1
                start_r = r
        if cnt_count >= m:
            for i in range(cnt_count):
                grid[start_r + i][c] = 0

def rotate():
    #1열 -> 1행, 1행 -> n열
    #n열 -> n행, n행 -> 1열
    temp_grid = [[0 for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            temp_grid[c][n - 1 - r] = grid[r][c]
    
    for r in range(n):
        for c in range(n):
            grid[r][c] = temp_grid[r][c]

def booom_fun():
    while True:
        prev = [row[:] for row in grid]
        booom()
        reset()
        if grid == prev:
            break

def print_grid():
    for row in grid:
        print(*row)
    print()

for _ in range(k):
    #print(f"-----------------------")
    booom_fun()
    #print_grid()

    rotate()
    reset()
    #print_grid()

booom_fun()
#print_grid()
    
ans = sum(1 for r in range(n) for c in range(n) if grid[r][c] != 0)

print(ans)







            

            
