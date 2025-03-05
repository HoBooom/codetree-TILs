x,y = map(int,input().split())

ans = 0

for i in range(x,y+1):
    temp = str(i)
    t_sum = 0
    for j in range(len(temp)):
        t_sum += int(temp[j])
    ans = max(ans,t_sum)

print(ans)
