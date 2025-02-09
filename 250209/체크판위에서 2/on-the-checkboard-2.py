R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Write your code here!

ans = 0

cnt_r,cnt_c = 0,0

def find_first_rc(color):
    find = []
    for r in range(1,R-2):
        for c in range(1,C - 2):
            if color == 'W':
                if grid[r][c] == 'B':
                    find.append((r,c))
            elif color == 'B':
                if grid[r][c] == 'W':
                    find.append((r,c))
    return find

def find_sec_rc(row,column,color):
    find = []
    for r in range(row + 1,R - 1):
        for c in range(column + 1,C - 1):
            if color == 'W':
                if grid[r][c] == 'B':
                    find.append((r,c))
            elif color == 'B':
                if grid[r][c] == 'W':
                    find.append((r,c))
    return find


first_points = find_first_rc(grid[0][0])


for _,(r,c) in enumerate(first_points):
    second_points = find_sec_rc(r,c,grid[r][c])
    ans += len(second_points)

print(ans)


