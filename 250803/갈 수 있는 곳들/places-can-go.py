from collections import deque

n, k = map(int,input().split())

grid = [
    list(map(int,input().split())) for _ in range(n)
]

visited = [
    [False for _ in range(n)] for _ in range(n)
]

queue = deque()

points = [
    tuple(map(int,input().split())) for _ in range(k)
]

drs, dcs = [0, 1, 0, -1],[1, 0 , -1, 0]


count = 0


def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

for s_r,s_c in points:
    s_r,s_c = s_r - 1, s_c - 1
    queue.appendleft((s_r,s_c))
    if not visited[s_r][s_c]:
        visited[s_r][s_c] = True
        count += 1
        while queue:
            cnt_r,cnt_c = queue.pop()

            for dr,dc in zip(drs,dcs):
                nr,nc = cnt_r + dr, cnt_c + dc
                if is_range(nr,nc) and not visited[nr][nc] and grid[nr][nc] == 0:
                    queue.appendleft((nr,nc))
                    visited[nr][nc] = True
                    count += 1

#print(*visited, sep="\n")

print(count)
    




