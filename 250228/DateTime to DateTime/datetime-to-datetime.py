
A,B,C = map(int,input().split())

ans = 0

cnt_d = 11
cnt_t = 11
cnt_m = 11

def f(A,B,C):
    temp = 0
    temp += A * 1440
    temp += B * 60
    temp += C
    return temp

if f(A,B,C) < f(cnt_d,cnt_m,cnt_t):
    print(-1)
else:
    while True:
        if cnt_d == A and cnt_t == B and cnt_m == C:
            break
        cnt_m += 1
        ans += 1
        if cnt_m == 60:
            cnt_t += 1
            cnt_m = 0
        if cnt_t == 24:
            cnt_d += 1
            cnt_t = 0
    print(ans)
