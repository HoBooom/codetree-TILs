n, m = map(int,input().split())

dias = [tuple(map(int,input().split())) for _ in range(n)]

ans = 0

dias.sort(key = lambda x: -x[1]/x[0])

for w,v in dias:
    if m >= w:
        m -= w
        ans += v
    else:
        ans += m * v / w
        break

print(f"{ans:.3f}")
