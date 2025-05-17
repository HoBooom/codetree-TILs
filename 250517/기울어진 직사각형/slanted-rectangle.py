n = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def get_score(r,c,k,l):
    drs,dcs = [-1,-1,1,1],[1,-1,-1,1]
    move_nums = [k,l,k,l]

    sum_of_nums = 0

    for dr,dc,move_num in zip(drs,dcs,move_nums):
        for _ in range(move_num):
            r, c = r + dr, c + dc

            if not is_range(r,c):
                return 0
            sum_of_nums += grid[r][c]
    return sum_of_nums

ans = 0

for r in range(n):
    for c in range(n):
        for k in range(1,n):
            for l in range(1,n):
                ans = max(ans,get_score(r,c,k,l))
print(ans)
