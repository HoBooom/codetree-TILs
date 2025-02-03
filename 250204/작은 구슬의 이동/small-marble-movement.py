n, t = map(int,input().split())
r,c,d = input().split()
r,c = int(r),int(c)

dirs = {
    'R' : 0,
    'L' : 2,
    'U' : 1,
    'D' : 3,
}
dir_num = dirs[d]

dc,dr = [1,0,-1,0],[0,-1,0,1]

def isRange(r,c):
    if 1<=r<=n and 1<=c<=n:
        return True
    return False

for i in range(t):
    n_r,n_c = r + dr[dir_num], c + dc[dir_num]

    if not isRange(n_r,n_c):
        dir_num = (dir_num + 2) % 4
        continue
    r,c = r + dr[dir_num],c + dc[dir_num]
    

print(r,c)

