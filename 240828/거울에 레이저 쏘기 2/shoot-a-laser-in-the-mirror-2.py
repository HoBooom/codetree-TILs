n = int(input())

board = [
    list(input()) for _ in range(n)
]

#print(board)

light = [
    [0 for _ in range(n)] for _ in range(n)
]

k = int(input())

dxs = [1,0,-1,0]
dys = [0,-1,0,1]

first_direct = k
if first_direct != 1:
    first_direct = (k - 1) // n
elif first_direct == 1:
    first_direct = 0

r,c = 0,0
if first_direct == 0:
    r = n -1
    c = k - 1
elif first_direct == 1:
    r = 2*n - k
    c = n - 1
elif first_direct == 2:
    r = 0
    c = 3*n - k
elif first_direct == 3:
    r = k - (3*n + 1)
    c = 0

ans = 1

def is_range(r,c):
    return 0<=r and r<n and 0<= c and c<n

def gogo(input_dir,r,c,ans):
    if is_range(r,c) == False:
        return ans 
    if input_dir == 0:#북
        if board[r][c] == '/':
            return 1,r,c-1,ans + 1
        else:
            return 3,r,c+1,ans + 1
    elif input_dir == 1:#동
        if board[r][c] == '/':
            return 0,r-1,c,ans + 1
        else:
            return 2,r+1,c,ans + 1
    elif input_dir == 2:#남
        if board[r][c] == '/':
            return 3,r,c+1,ans + 1
        else:
            return 1,r,c-1,ans + 1
    elif input_dir == 3:#서
        if board[r][c] == '/':
            return 2,r+1,c,ans + 1
        else:
            return 0,r-1,c,ans + 1


final_ans,r,c,ans = (gogo(first_direct,r,c,ans))
print(final_ans)