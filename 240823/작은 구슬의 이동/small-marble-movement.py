n,t = map(int,input().split())
r,c,d = input().split()
r = int(r) - 1
c = int(c) - 1

directs = {
    "U" : 0,
    "R" : 1,
    "D" : 2,
    "L" : 3,
}


def is_range(x,y):
    return 0<= x and x<n and 0<=y and y<n

drs = [-1,0,1,0]
dcs = [0,1,0,-1]

direct = directs[d]

for i in range(t):
    nr,nc = r + drs[direct], c + dcs[direct]
    if is_range(nc,nr):
        r,c = nr,nc
    else:
        direct = (direct + 2) % 4
        

print(r + 1,c + 1)