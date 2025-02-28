n = int(input())

cnt_x = cnt_y = 0

dx,dy = [1,0,-1,0],[0,-1,0,1]
dir_num = ['E','S','W',"N"]

for _ in range(n):
    dir_n, t = input().split()
    t = int(t)
    for i in range(4):
        if dir_n == dir_num[i]:
            cnt_x,cnt_y = cnt_x + t*dx[i],cnt_y + t*dy[i]

print(cnt_x,cnt_y)