n = int(input())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

biggest_block = 0
boom_count = 0
cnt_count = 0

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def boom(r,c,num):
    global cnt_count, biggest_block, boom_count
    
    if visited[r][c] or grid[r][c] != num:
        return
    
    visited[r][c] = True
    cnt_count += 1

    drs, dcs = [0,1,0,-1],[1,0,-1,0]

    for dr,dc in zip(drs,dcs):
        nr,nc = r + dr, c + dc
        if is_range(nr,nc):
            boom(nr,nc,num)


for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            cnt_count = 0
            boom(r,c,grid[r][c])
            biggest_block = max(biggest_block, cnt_count)
            if cnt_count >= 4:
                boom_count += 1

print(boom_count, biggest_block)
        
