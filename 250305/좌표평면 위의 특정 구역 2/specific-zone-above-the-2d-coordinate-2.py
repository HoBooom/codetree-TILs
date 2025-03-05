import sys

INT_MAX = sys.maxsize

n = int(input())

points = [tuple(map(int,input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = INT_MAX

for i in range(n):
    max_x = max(x[:i] + x[i + 1:])
    max_y = max(y[:i] + y[i + 1:])
    min_x = min(x[:i] + x[i + 1:])
    min_y = min(y[:i] + y[i + 1:])

    area = (max_x - min_x) * (max_y - min_y)
    ans = min(ans,area)

print(ans)


