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

board = [
    [0 for _ in range(n)] for _ in range(n)
]

def is_range(x,y):
    return 0<= x and x<n and 0<=y and y<n

dxs = [0,1,0,-1]
dys = [-1,0,1,0]

direct = directs[d]

for i in range(t):
    nr,nc = r + dxs[direct], c + dys[direct]
    if is_range(nr,nc):
        r,c = nr,nc
    else:
        direct = (direct + 2) % 4
        

print(c,r)