dirs = input()

# Please write your code here.
dx,dy = [0,-1,0,1],[1,0,-1,0]
dir_num = 0

cnt_x = cnt_y = 0

dirs = list(dirs)

for i in range(len(dirs)):
    if dirs[i] == 'L':
        dir_num = (dir_num + 1) % 4
    elif dirs[i] == 'R':
        dir_num = (dir_num - 1) % 4
    elif dirs[i] == 'F':
        cnt_x,cnt_y = cnt_x + dx[dir_num], cnt_y + dy[dir_num]

print(cnt_x,cnt_y)
 