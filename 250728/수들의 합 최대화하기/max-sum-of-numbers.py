n = int(input())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

max_val = max(max(nums) for nums in grid)

#각 행 열에 하나씩 오려면 r도 겹치면 안되고 c도 겹치면 안됨
# visited_r = [False] * n
# visited_c = [False] * n
visited = [False] * n

selected_nums = []

ans = 0

def calc():
    return sum(selected_nums)

def choose(cnt):
    global ans, max_val

    if sum(selected_nums) + (n - cnt) * max_val < ans:
        return

    if cnt == n:
        ans = max(ans, calc())
        return

    for i in range(n):
        if visited[i]:
            continue
        
        selected_nums.append(grid[cnt][i])
        visited[i] = True

        choose(cnt + 1)
        selected_nums.pop()
        visited[i] = False

    # for r in range(n):
    #     if visited_r[r]:
    #         continue
    #     for c in range(n):
    #         if visited_c[c]:
    #             continue
            
    #         selected_nums.append(grid[r][c])
    #         visited_r[r] = True
    #         visited_c[c] = True
    #         choose(cnt + 1)

    #         selected_nums.pop()
    #         visited_r[r] = False
    #         visited_c[c] = False
    
    return

choose(0)
print(ans)

            
