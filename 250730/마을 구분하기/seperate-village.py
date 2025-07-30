n = int(input())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

village = []

count = 0

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def can_go(r,c):
    if not is_range(r,c):
        return False
    if visited[r][c] or grid[r][c] == 0:
        return False
    return True


def count_village(r,c):
    global count
    drs, dcs = [0,1,0,-1],[1,0,-1,0]

    visited[r][c] = True
    count += 1

    for dr, dc in zip(drs,dcs):
        nr,nc = r + dr, c + dc
        if can_go(nr,nc):
            count_village(nr,nc)

for r in range(n):
    for c in range(n):
        count = 0
        if can_go(r,c):
            count_village(r,c)
            village.append(count)

village.sort()

print(len(village))
print(*village, sep="\n")

            







