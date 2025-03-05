n,k = map(int,input().split())

arr = list(map(int,input().split()))

ans = 0

for i in range(n):
    temp = sum(arr[i:i + k])
    
    ans = max(ans,temp)

print(ans)
    