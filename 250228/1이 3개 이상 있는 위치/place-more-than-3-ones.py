n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def is_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

ans = 0

dr,dc = [0,1,0,-1],[1,0,-1,0]
for r in range(n):
    for c in range(n):
        count = 0
        for dir_n in range(4):
            nr,nc = r + dr[dir_n], c + dc[dir_n]
            if is_range(nr,nc):
                if grid[nr][nc] == 1:
                    count += 1
        if count >= 3:
            ans += 1
print(ans)
