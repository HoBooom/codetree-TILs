n = int(input())

dx,dy = [1,0,-1,0],[0,-1,0,1]

cnt_x,cnt_y = 0,0

def dir_num(d):
    if d=="E":
        return 0
    elif d=="S":
        return 1
    elif d=="W":
        return 2
    elif d =="N":
        return 3

for _ in range(n):
    dr,xi = input().split()
    dir_n = dir_num(dr)
    xi = int(xi)

    cnt_x,cnt_y = cnt_x + xi*dx[dir_n], cnt_y + xi*dy[dir_n]

print(cnt_x,cnt_y)