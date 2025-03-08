n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

r,c = map(int,input().split())

def is_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

def boom(r,c):
    boom = board[r][c]
    board[r][c] = 0
    dr,dc = [0,1,0,-1],[1,0,-1,0]
    for dir_num in range(4):
        temp_r,temp_c = r,c
        for i in range(boom - 1):
            nr,nc = temp_r + dr[dir_num], temp_c + dc[dir_num]
            if is_range(nr,nc):
                board[nr][nc] = 0
            else:
                break
            temp_r,temp_c = nr,nc

def sort(board):
    for c in range(n):
        is_sort = False
        temp = []
        for i in range(n):
            if board[n - i - 1][c] != 0:
                temp.append(board[n - i - 1][c])
        while len(temp) < n:
            temp.append(0)
        for i in range(n):
            board[n - i - 1][c] = temp[i]

boom(r-1,c-1)
sort(board)



for _,item in enumerate(board):
    print(*item)