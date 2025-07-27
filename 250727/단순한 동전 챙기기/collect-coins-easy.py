import sys

INT_MAX = sys.maxsize
COIN_N = 9

n = int(input())

grid = [
    input() for _ in range(n)
]

coins = []
selected_coins = []
start_point = [-1,-1]
end_point = [-1,-1]

ans = INT_MAX


for r in range(n):
    for c in range(n):
        if grid[r][c] != '.':
            if grid[r][c] == 'S':
                start_point = [r,c]
            elif grid[r][c] == 'E':
                end_point = [r,c]

for num in range(COIN_N + 1):
    for r in range(n):
        for c in range(n):
            if grid[r][c] == str(num):
                coins.append([r,c])

def dist(a,b):
    (a_r,a_c),(b_r,b_c) = a,b
    return abs(a_r - b_r) + abs(a_c - b_c)

def calc():
    moved = dist(start_point, selected_coins[0])
    for i in range(3 - 1):
        moved += dist(selected_coins[i], selected_coins[i + 1])
    moved += dist(selected_coins[2], end_point)
    return moved

def f(cur_idx, cnt):
    global ans

    if cnt == 3:
        ans = min(ans,calc())
        return 
    
    if cur_idx == len(coins):
        return
    
    f(cur_idx + 1, cnt)

    selected_coins.append(coins[cur_idx])
    f(cur_idx + 1, cnt + 1)
    selected_coins.pop()

f(0,0)

if ans == INT_MAX:
    ans = -1

print(ans)




