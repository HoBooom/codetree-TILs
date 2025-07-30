n , m = map(int,input().split())

village = [
    list(map(int,input().split())) for _ in range(n)
]
cnt_village = [row[:] for row in village]

visited = [[False for _ in range(m)] for _ in range(n)]

max_depth = max(max(homes) for homes in village)

area = [0] * (max_depth + 1)
count = 0

def is_range(r,c):
    return 0 <= r < n and 0 <= c < m

def set_village(k):
    for r in range(n):
        for c in range(m):
            cnt_village[r][c] = village[r][c] - k
            if cnt_village[r][c] < 0:
                cnt_village[r][c] = 0
    return 

def can_go(r,c):
    if not is_range(r,c):
        return False
    if visited[r][c] or cnt_village[r][c] == 0:
        return False
    return True

def find_area(r,c):
    drs, dcs = [0,1,0,-1],[1,0,-1,0]

    visited[r][c] = True

    for dr, dc in zip(drs,dcs):
        nr,nc = r + dr, c + dc
        if can_go(nr,nc):
            find_area(nr,nc)



for k in range(1, max_depth + 1):
    visited = [[False for _ in range(m)] for _ in range(n)]
    set_village(k)
    # print(k)
    # print(*cnt_village, sep="\n")
    # print("-" * 10) 
    count = 0
    for r in range(n):
        for c in range(m):
            if can_go(r,c):
                count += 1
                find_area(r,c)
    area[k] = count

ans_k, ans_area = -1, -1

for i in range(len(area)):
    if ans_area < area[i]:
        ans_area = area[i]
        ans_k = i

print(ans_k, ans_area)





