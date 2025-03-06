N,C,G,H = map(int,input().split())

temperatures = [tuple(map(int,input().split())) for _ in range(N)]

ans = 0

def output(t,T_a,T_b):
    if t < T_a:
        return C
    elif T_a <= t <= T_b:
        return G
    elif t > T_b:
        return H

    

for i in range(1001):
    total = 0
    total = sum([output(i,T_a,T_b) for T_a,T_b in temperatures])
    ans = max(ans,total)


    

print(ans)
    