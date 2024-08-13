n,m,k = map(int,input().split())

student = [0 for _ in range(n + 1)]

ans = []
ans.append(-1)

for _ in range(m):
    target = int(input())
    student[target] += 1
    if student[target] >= k:
        ans.append(target)

if len(ans) == 1:
    print(ans[0])
elif len(ans) > 1:
    print(ans[1])