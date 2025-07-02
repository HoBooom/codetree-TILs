n,m,r,c = map(int,input().split())
r,c = r - 1, c - 1

commands = list(map(str,input().split()))

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

up, front, right = 1,2,3

def move(command,up,front,right):
    if command == 'U':
        return front, 7-up, right
    elif command == 'D':
        return 7-front, up, right
    elif command == 'R':
        return 7-right, front, up
    elif command == 'L':
        return right, front, 7-up

def move_idx(r,c,command):
    if command == 'U':
        return r - 1, c
    elif command == 'D':
        return r + 1, c
    elif command == 'R':
        return r, c + 1
    elif command == 'L':
        return r, c - 1

def print_grid():
    for r in grid:
        print(*r)

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

grid[r][c] = 6

for command in commands:
    nr,nc = move_idx(r,c,command)
    if is_range(nr,nc):
        r,c = nr,nc
        up,front,right = move(command,up,front,right)
        grid[r][c] = 7 - up

#print_grid()
    
ans = sum(grid[i][j] for i in range(n) for j in range(n))

print(ans)