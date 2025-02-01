dirs = input()

# Write your code here!

dirs = list(dirs)

cnt_x,cnt_y = 0,0

dx,dy = [0,1,0,-1],[1,0,-1,0]
dir_num = 0

for elem in dirs:
    if elem == 'R':
        dir_num = (dir_num + 1) % 4
    elif elem =='L':
        dir_num = (dir_num - 1) % 4
    elif elem =='F':
        cnt_x,cnt_y = cnt_x + dx[dir_num],cnt_y + dy[dir_num]

print(cnt_x,cnt_y)
