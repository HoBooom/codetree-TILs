N,M,T,K = map(int,input().split())

balls = []
for idx in range(M):
    r,c,direct,speed = map(str,input().split())

    if direct == 'U':
        direct = 0
    elif direct == 'D':
        direct = 3
    elif direct == 'R':
        direct = 1
    elif direct == 'L':
        direct = 2

    balls.append([idx + 1,int(r) - 1,int(c) - 1,direct,int(speed)])

grid = [
    [[] for _ in range(N)]
    for _ in range(N)
]



#U R L D
drs,dcs = [-1,0,0,1],[0,1,-1,0]

def is_range(r,c):
    return 0<=r<N and 0<=c<N

def move_ball(ball):
    idx,r,c,direct,speed = ball

    for _ in range(speed):
        nr,nc = r + drs[direct], c + dcs[direct]
        if not is_range(nr,nc):
            direct = 3 - direct
            nr,nc = r + drs[direct], c + dcs[direct]
        r,c = nr,nc
    return idx,r,c,direct,speed


def move_all_ball(balls):
    temp_grid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for ball in balls:
        idx,r,c,dir_n,speed = move_ball(ball)
        temp_grid[r][c].append([idx,r,c,dir_n,speed])

    new_balls = []
    for r in range(N):
        for c in range(N):
            if len(temp_grid[r][c]) > K:
                temp_grid[r][c].sort(key = lambda x : (-x[4],-x[0]))
                temp_grid[r][c] = temp_grid[r][c][:K]
            new_balls.extend(temp_grid[r][c])
    return new_balls
    
for _ in range(T):
    balls = move_all_ball(balls)

print(len(balls))