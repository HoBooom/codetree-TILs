from collections import deque

n,m = map(int,input().split())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

visited = [
    [False for _ in range(m)] for _ in range(n)
]


def is_range(r,c):
    return 0 <= r < n and 0 <= c < m

queue = deque()

queue.appendleft((0,0))
visited[0][0] = True

drs,dcs = [0,1,0,-1],[1,0,-1,0]

while True:
    if len(queue) == 0:
        break
    
    cnt_r,cnt_c = queue.pop()
    

    for dr, dc in zip(drs,dcs):
        nr,nc = cnt_r + dr, cnt_c + dc
        if is_range(nr,nc) and not visited[nr][nc] and grid[nr][nc] != 0:
            queue.appendleft((nr,nc))
            visited[nr][nc] = True

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)



