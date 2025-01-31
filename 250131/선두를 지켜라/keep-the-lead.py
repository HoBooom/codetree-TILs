n, m = map(int, input().split())

# Process A's movements
a_point = []
a_point.append(0)
a_cnt = 0

for _ in range(n):
    v1,ti = map(int,input().split())
    for _ in range(ti):
        a_cnt += v1
        a_point.append(a_cnt)

# Process B's movements
b_point = []
b_point.append(0)
b_cnt =0

for _ in range(m):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        b_cnt += vi
        b_point.append(b_cnt)

def check(a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return 2

#print(a_point)
#print(b_point)

beforeSituation = check(a_point[1],b_point[1])
ans = 0
beforeFirst = beforeSituation

for i in range(2,len(a_point)):
    cnt_check = check(a_point[i],b_point[i])
    cnt_first = cnt_check
    if cnt_check != beforeSituation:
        if beforeFirst == 0:
            beforeFirst = cnt_first
            continue
        if cnt_first != 0 and beforeFirst != cnt_first:
            ans += 1
            beforeFirst = cnt_first
    beforeSituation = cnt_check

print(ans)


