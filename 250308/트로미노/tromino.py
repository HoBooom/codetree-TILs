r,c = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(r)]

def is_range(row,column):
    if 0 <= row < r and 0 <= column < c:
        return True
    return False

def check1(i,j):
    dr,dc = [-1,0,1,0],[0,1,0,-1]
    cnt_max = 0
    for dir_num in range(4):
        r1, c1 = i + dr[dir_num], j + dc[dir_num]
        r2, c2 = i + dr[(dir_num + 1) % 4], j + dc[(dir_num + 1) % 4]
        if is_range(r1, c1) and is_range(r2, c2):
            box = board[i][j] + board[r1][c1] + board[r2][c2]
            cnt_max = max(cnt_max, box)
    return cnt_max

def check2(i,j):
    box1 = box2 = 0
    if j <= c - 3:
        box1 = board[i][j] + board[i][j + 1] + board[i][j + 2]
    if i <= r - 3:
        box2 = board[i][j] + board[i + 1][j] + board[i + 2][j]
    return max(box1,box2)

ans = 0

for i in range(r):
    for j in range(c):
        ans = max(ans,check1(i,j),check2(i,j))

print(ans)

