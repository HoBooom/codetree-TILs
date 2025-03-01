commands = input()
commands = list(commands)

# Write your code here!

first_x = first_y = cnt_x = cnt_y = 0

dx,dy = [0,1,0,-1],[1,0,-1,0]
dir_num = 0
time = 0

isMove = False
ans = -1


for _,command in enumerate(commands):
    isEnd = False
    if command == 'R':
        dir_num = (dir_num + 1) % 4
    elif command == 'L':
        dir_num = (dir_num - 1) % 4
    elif command == 'F':
        cnt_x,cnt_y = cnt_x + dx[dir_num],cnt_y + dy[dir_num]
        isMove = True
    time += 1
    #print(cnt_x,cnt_y)
    if time != 0 and (cnt_x,cnt_y) == (0,0) and isMove:
        ans = time
        isEnd = True
    if isEnd:
        break   

print(ans)

