import sys

INT_MAX = sys.maxsize

n,m = map(int,input().split())

points = [
    tuple(map(int,input().split())) for _ in range(n)
]

select_points = []
ans = INT_MAX

def dist(a,b):
    (a_x, a_y), (b_x, b_y) = a, b
    return (((a_x - b_x) ** 2) + ((a_y - b_y) ** 2))

def calc():
    min_dist = 0

    for i in range(m - 1):
        for j in range(i + 1, m):
            min_dist = max(min_dist, dist(select_points[i], select_points[j]))

    return (min_dist)

def choose(cur_idx, cnt):
    global ans

    if cnt == m:
        ans = min(ans, calc())
        return 
    
    if cur_idx == n:
        return 
    
    choose(cur_idx + 1, cnt)
    select_points.append(points[cur_idx])

    choose(cur_idx + 1, cnt + 1)
    select_points.pop()

choose(0,0)
print(ans)

