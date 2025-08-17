from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

jump = [
    [0 for _ in range(n)] for _ in range(n)
]

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

ans = -1

# Please write your code here.

drs, dcs = [-2,-1,1,2,2,1,-1,-2],[1,2,2,1,-1,-2,-2,-1]

queue = deque()
queue.append((r1-1, c1-1))

while queue:
    cnt_r,cnt_c = queue.pop()

    for dr,dc in zip(drs,dcs):
        nr,nc = cnt_r + dr, cnt_c + dc
        if is_range(nr,nc):
            if jump[nr][nc] == 0:
                jump[nr][nc] = jump[cnt_r][cnt_c] + 1
                queue.appendleft((nr,nc))
            elif jump[nr][nc] > jump[cnt_r][cnt_c] + 1:
                jump[nr][nc] = jump[cnt_r][cnt_c] + 1
                queue.appendleft((nr,nc))

if (r1,c1) == (r2,c2):
    print(0)
elif jump[r2-1][c2-1] == 0:
    print(-1)
else:
    print(jump[r2-1][c2-1])


