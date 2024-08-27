n = int(input())

board = [
    list(input()) for _ in range(n)
]


k = int(input())

r,c = 0,0

if k <= n:
    r = n - 1
    c = k - 1
    first_direct = 0
elif k <= 2 * n:
    r = 2 * n - k
    c = n - 1
    first_direct = 1
elif k <= 3 * n:
    r = 0
    c = 3 * n - k
    first_direct = 2
else:
    r = k - 3 * n - 1
    c = 0
    first_direct = 3

def is_range(r, c):
    return 0 <= r < n and 0 <= c < n

ans = 1

def is_range(r,c):
    return 0<=r and r<n and 0<= c and c<n

def gogo(input_dir,r,c,ans):
    if is_range(r,c) == False:
        return ans 
    if input_dir == 0:#북
        if board[r][c] == '/':
            return gogo(1,r,c-1,ans + 1)
        else:
            return gogo(3,r,c+1,ans + 1)
    elif input_dir == 1:#동
        if board[r][c] == '/':
            return gogo(0,r-1,c,ans + 1)
        else:
            return gogo(2,r+1,c,ans + 1)
    elif input_dir == 2:#남
        if board[r][c] == '/':
            return gogo(3,r,c+1,ans + 1)
        else:
            return gogo(1,r,c-1,ans + 1)
    elif input_dir == 3:#서
        if board[r][c] == '/':
            return gogo(2,r+1,c,ans + 1)
        else:
            return gogo(0,r-1,c,ans + 1)


#final_ans,r,c,ans = (gogo(first_direct,r,c,ans))
final_ans = (gogo(first_direct,r,c,ans))
print(final_ans)