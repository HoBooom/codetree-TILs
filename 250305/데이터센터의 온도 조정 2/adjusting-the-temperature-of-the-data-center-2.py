N,C,G,H = map(int,input().split())

temperatures = [tuple(map(int,input().split())) for _ in range(N)]

ans = 0

for i in range(1001):
    charge = 0
    for idx,(t1,t2) in enumerate(temperatures):
        if i < t1:
            charge += C
        elif t1 <= i <= t2:
            charge += G
        elif i > t2:
            charge +=H
    ans = max(ans,charge)

print(ans)
    