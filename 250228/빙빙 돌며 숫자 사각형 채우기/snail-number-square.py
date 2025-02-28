n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dr,dc = [0,1,0,-1],[1,0,-1,0]

def is_range(r,c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False

dir_num = 0
cnt_num = 1
cnt_r,cnt_c = 0,-1
while True:
    if cnt_num > n * m:
        break
    nr,nc = cnt_r + dr[dir_num], cnt_c + dc[dir_num]
    if is_range(nr,nc) and arr[nr][nc] == 0:
        arr[nr][nc] = cnt_num
        cnt_num += 1
        cnt_r,cnt_c = nr,nc
    else:
        dir_num = (dir_num + 1) % 4

for r in range(n):
    for c in range(m):
        print(arr[r][c], end = " ")
    print()