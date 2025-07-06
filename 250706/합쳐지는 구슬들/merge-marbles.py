N, M, T = map(int,input().split())

balls = []


mapper = {
    "U" : 0,
    "D" : 3,
    "R" : 1,
    "L" : 2
}
drs,dcs = [-1, 0, 0, 1], [0, 1, -1, 0]

for i in range(M):
    r,c,d,w = map(str,input().split())
    r,c,w = int(r) - 1,int(c) - 1,int(w)
    dir_n = mapper[d]
    balls.append([r,c,dir_n,w,i+1])


def is_range(r,c):
    return 0 <= r < N and 0 <= c < N

def move(ball):
    r,c,d,w,i = ball
    nr,nc = r + drs[d], c + dcs[d]
    if not is_range(nr,nc):
        d = 3 - d
        nr,nc = r + drs[d], c + dcs[d]
    if not is_range(nr,nc):
        d = 3 - d
        nr,nc = r,c
    return [nr,nc,d,w,i]

def move_all_balls():
    temp_grid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for ball in balls:
        moved_ball = move(ball)
        nr,nc,_,_,_ = moved_ball
        temp_grid[nr][nc].append(moved_ball)

    next_balls = []
    for r in range(N):
        for c in range(N):
            if len(temp_grid[r][c]) == 1:
                next_balls.append(temp_grid[r][c][0])
            elif len(temp_grid[r][c]) >= 2:
                weight_sum = sum(ball[3] for ball in temp_grid[r][c])
                temp_grid[r][c].sort(key = lambda x : -x[4])
                _,_,dir_num,_,ball_id = temp_grid[r][c][0]
                next_balls.append([r,c,dir_num,weight_sum,ball_id])
    
    #print(*next_balls)
    return next_balls

def print_grid(balls):
    temp_grid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for ball in balls:
        nr,nc,_,_,i = ball
        temp_grid[nr][nc].append(i)
    
    for r in temp_grid:
        print(*r)
    print("-----------")


for _ in range(T + 1):
    #print_grid(balls)
    #print(*balls)
    balls = move_all_balls()
    #print_grid(balls)
    #print()
    #print("------------------------")

balls.sort(key = lambda x : -x[3])
print(len(balls), balls[0][3])
