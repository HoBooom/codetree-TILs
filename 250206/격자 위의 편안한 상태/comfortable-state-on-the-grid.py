n, m = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]


# Write your code here!

def is_range(r,c):
    if 0 <= r < n and 0<= c < n:
        return True
    return False

def check(r,c):
    dr,dc = [0,-1,0,1],[1,0,-1,0]
    count = 0
    for i in range(4):
        temp_r,temp_c = r + dr[i],c + dc[i]
        if is_range(temp_r,temp_c):
            if board[temp_r][temp_c] == 1:
                count += 1
    if count == 3:
        return True
    return False

ans = 0

for _ in range(m):
    cr,cc = map(int,input().split())
    cr -= 1 
    cc -= 1
    board[cr][cc] = 1
    if check(cr,cc):
        print(1)
    else:
        print(0)


