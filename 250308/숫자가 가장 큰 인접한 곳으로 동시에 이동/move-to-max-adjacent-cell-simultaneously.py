n, m, t = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

balls = []
for _ in range(m):
    a,b = map(int,input().split())
    balls.append((a - 1,b - 1))
#print(balls)

dr,dc = [-1,1,0,0],[0,0,-1,1]

ans = 0

def is_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

def check(r,c):
    max_n = 0
    t_r,t_c = (0,0)
    for dir_num in range(4):
        nr,nc = r + dr[dir_num], c + dc[dir_num]
        if is_range(nr,nc):
            if max_n < board[nr][nc]:
                t_r,t_c = nr,nc
                max_n = board[nr][nc]
    return t_r,t_c


for time in range(t):
    temp_dic = {}

    for i in range(len(balls)):
        balls[i] = check(balls[i][0],balls[i][1])

    new_balls = []
    for item in (balls):
        temp_dic[item] = temp_dic.get(item,0) + 1
    for key,value in temp_dic.items():
        if value == 1:
            new_balls.append(key)
    balls = new_balls
    #print(balls)

print(len(balls))
        

                

        
    
