n,t = map(int,input().split())

commands = list(input())

board = [
    list(map(int,input().split())) for _ in range(n)
]

center = n // 2
r = c = center

drs = [-1,0,1,0]
dcs = [0,1,0,-1]
direct = 0 

ans = board[r][c]

def is_range(r,c):
    return 0<=r<n and 0<=c<n

for i,command in enumerate(commands):
    if command == "R":
        direct = (direct + 1) % 4
    elif command == "L":
        direct = (direct + 3) % 4
    elif command =="F":
        nr,nc = r + drs[direct], c + dcs[direct]
        if is_range(nr,nc):
            r,c = nr,nc
            ans += board[r][c]

print(ans)