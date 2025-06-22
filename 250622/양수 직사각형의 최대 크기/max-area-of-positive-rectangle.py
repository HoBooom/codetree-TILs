n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

def check_pos_rect(x1,y1,x2,y2):
    for x in range(x1,x2 + 1):
        for y in range(y1,y2 + 1):
            if board[x][y] <= 0:
                return False
    return True

def rect_size(x1,y1,x2,y2):
    return (x2 - x1 + 1) * (y2 - y1 + 1)

def find_pos_max():
    max_sum = 0

    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    if check_pos_rect(i,j,k,l):
                        max_sum = max(max_sum, rect_size(i,j,k,l))
    return max_sum if max_sum != 0 else -1

ans = find_pos_max()
print(ans)

    