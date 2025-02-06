n = int(input())
grid = [list(input()) for _ in range(n)]
cnt = int(input())
cnt -= 1

# Write your code here!

def razer(window,di):
    if window == '\\':
        if di == 0:
            return 1
        elif di == 1:
            return 0
        elif di == 2:
            return 3
        elif di == 3:
            return 2
    elif window == '/':
        if di == 0:
            return 3
        elif di == 1:
            return 2
        elif di == 2:
            return 1
        elif di == 3:
            return 0

def first_position(cnt):
    r,c = 0,0
    dr,dc = [0,1,0,-1],[1,0,-1,0]
    dir_num = 0
    #print(f'first_position {cnt}')
    for i in range(cnt):
        #print(i)
        if i == 0:
            None
        elif i % 3 == 0:
            dir_num += 1
            #print('dir change')
            continue
        r,c = r + dr[dir_num],c + dc[dir_num]
        #print(r,c)
    return r,c
        

def is_range(r,c):
    if 0<= r < n and 0 <= c < n:
        return True
    return False

cnt_r,cnt_c = first_position(cnt)

ans = 0
input_dir = cnt // 3

while True:
    if is_range(cnt_r,cnt_c):
        
        output_dir = razer(grid[cnt_r][cnt_c],input_dir)
        ans += 1
        dr,dc = [0,1,0,-1],[1,0,-1,0]
        cnt_r,cnt_c = cnt_r + dr[output_dir],cnt_c + dc[output_dir]
        # 1 => 3,0 => 2, 2 => 0, 3 => 1
        input_dir = razer('\\',output_dir)
    else:
        break

print(ans)



