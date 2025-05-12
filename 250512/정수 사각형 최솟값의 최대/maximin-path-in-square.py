import sys

INT_MAX = sys.maxsize

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

#1이면 왼쪽, 2이면 위쪽
dir_board = [[0 for _ in range(n)] for _ in range(n)]

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

for r in range(n):
    for c in range(n):
        if r == 0 and c == 0:
            continue
        if not is_range(r-1,c): #위쪽이 없음
            dir_board[r][c] = 1
        elif not is_range(r,c-1): #왼쪽이 없음
            dir_board[r][c] = 2
        else:
            if board[r-1][c] >= board[r][c-1]:
                dir_board[r][c] = 2
            else:
                dir_board[r][c] = 1

ans = INT_MAX
cnt_r,cnt_c = n-1,n-1

while True:
    if cnt_r == 0 and cnt_c == 0:
        ans = min(ans,board[cnt_r][cnt_c])
        break
    ans = min(ans,board[cnt_r][cnt_c])
    if dir_board[cnt_r][cnt_c] == 1:
        cnt_c -= 1
    else:
        cnt_r -= 1

print(ans)
        
        
