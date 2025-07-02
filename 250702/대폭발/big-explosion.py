n,m,r,c = map(int,input().split())
r,c = r - 1,c - 1

grid = [[0 for _ in range(n)] for _ in range(n)]

def is_range(r,c):
    return 0<=r<n and 0<=c<n

def boom(r,c,t):
    if t == m + 1:
        return
    drs,dcs = [-1, 0 ,1, 0], [0, 1, 0, -1]
    for dr,dc in zip(drs,dcs):
        cnt_dis = 2 ** (t - 1)
        nr,nc = r + (dr * cnt_dis), c + (dc * cnt_dis)
        if is_range(nr,nc):
            grid[nr][nc] = 1
            boom(nr,nc,t + 1)
    
    return boom(r,c,t + 1)

def print_grid():
    for r in grid:
        print(*r)

grid[r][c] = 1
boom(r,c,1)
# for t in range(1,m + 1):
#     print()
#     for i in range(n):
#         for j in range(n):
#             if grid[i][j] == 1:
#                 boom(i,j,t)
#     print_grid()

#print_grid()
ans = sum(grid[i][j] for i in range(n) for j in range(n))

print(ans)



    
