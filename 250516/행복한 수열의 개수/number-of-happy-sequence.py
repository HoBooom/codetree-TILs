n, m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

def check_r(r):
    cnt_count = 1
    cnt_i = 0
    for i in range(1,n):
        if board[r][cnt_i] == board[r][i]:
            cnt_count += 1
        else:
            if cnt_count >= m:
                return 1
            cnt_count = 1
            cnt_i = i
    if cnt_count >= m:
        return 1
    return 0

def check_c(c):
    cnt_count = 1
    cnt_i = 0
    for i in range(1,n):
        if board[cnt_i][c] == board[i][c]:
            cnt_count += 1
        else:
            if cnt_count >= m:
                return 1
            cnt_count = 1
            cnt_i = i
    if cnt_count >= m:
        return 1
    return 0

ans = 0

#print(*board,sep="\n")
for i in range(n):
    ans += check_r(i)
    ans += check_c(i)

print(ans)



            