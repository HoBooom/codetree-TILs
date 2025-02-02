n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

dx,dy = [1,0,-1,0],[0,-1,0,1]

ans = 0

for r in range(n):
    for c in range(n):
        count = 0
        for dir_num in range(4):
            check_x = r + dx[dir_num]
            check_y = c + dy[dir_num]
            if 0 <= check_x < n and 0 <= check_y < n:
                if grid[check_x][check_y] == 1:
                    count += 1
        if count >= 3:
            ans += 1

print(ans)
            

            
            