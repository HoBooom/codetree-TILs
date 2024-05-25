list0=list(map(str,input().split()))

ans=0

for i in range(len(list0)):
    ans += len(list0[i])

print(ans)