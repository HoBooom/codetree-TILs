
n = int(input())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

ans = 0

selected_nums = []

visited = [False] * n

def choose(row):
    global ans 

    if row == n:
        ans = max(ans, min(selected_nums))
        return

    for c in range(n):
        if visited[c]:
            continue
        visited[c] = True
        selected_nums.append(grid[row][c])

        choose(row + 1)

        visited[c] = False
        selected_nums.pop()

    return

choose(0)
print(ans)
        
        
        
