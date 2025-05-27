n, m = map(int,input().split())

dias = []

for _ in range(n):
    w,v = map(float,input().split())
    cost = v / w
    dias.append([w,v,cost])

dias.sort(key = lambda x : x[2])

ans = 0
cnt = 0

for i in reversed(range(n)):
    isEnd = False
    while dias[i][0] > 0:
        if cnt == m:
            isEnd = True
            break
        ans += dias[i][2]
        dias[i][0] -= 1
        cnt += 1

    if isEnd:
        break

print(f"{ans:.3f}")

