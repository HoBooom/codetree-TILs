n = int(input())
grid = [list(input()) for _ in range(n)]
cnt = int(input())

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
    for i in range(0,cnt):
        if i == 0:
            None
        elif i % n == 0:
            dir_num += 1
        else:
            r,c = r + dr[dir_num],c + dc[dir_num]
    return r,c
        

def is_range(r,c):
    if 0<= r < n and 0 <= c < n:
        return True
    return False

cnt_r,cnt_c = first_position(cnt)

ans = 0
input_dir = (cnt - 1) // n

while True:
    if is_range(cnt_r,cnt_c):
        output_dir = razer(grid[cnt_r][cnt_c],input_dir)
        ans += 1
        dr,dc = [-1,0,1,0],[0,1,0,-1]
        #print(f'cnt {grid[cnt_r][cnt_c]}, input {input_dir} output {output_dir} before {cnt_r} {cnt_c}',end= " ")
        cnt_r,cnt_c = cnt_r + dr[output_dir],cnt_c + dc[output_dir]
        #print(f'next {cnt_r} {cnt_c}')
        # 1 => 3,0 => 2, 2 => 0, 3 => 1
        if output_dir == 0:
            input_dir = 2
        elif output_dir == 2:
            input_dir = 0
        elif output_dir == 1:
            input_dir = 3
        elif output_dir == 3:
            input_dir = 1
    else:
        break

print(ans)



