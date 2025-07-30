n, m = map(int,input().split())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

visited = [
    [False for _ in range(m)] for _ in range(n)
]

is_arrived = False

def is_range(r,c):
    return 0 <= r < n and 0 <= c < m

def can_go(r,c):
    if not is_range(r,c):
        return False
    if grid[r][c] == 0:
        return False
    return True                                


def gogo(r,c):
    global is_arrived

    if r == n - 1 and c == m - 1:
        # print("yes")
        is_arrived = True
    if is_arrived:
        return 
    
    drs, dcs = [0,1], [1,0]

    # visited[r][c] = True

    for dr,dc in zip(drs,dcs):
        nr, nc = r + dr, c + dc
        if can_go(nr,nc):
            gogo(nr, nc)
            # print(nr,nc)

gogo(0,0)

if is_arrived:
    print(1)
else:
    print(0)