n = int(input())

arr = list(map(int,input().split()))

min_arr = min(arr)
max_arr = max(arr)

ans = 0

for k in range(min_arr + 1, max_arr):
    count = 0
    for i in range(n):
        for j in range(i + 1,n):
            if abs(arr[i] - k) == abs(k - arr[j]):
                count += 1
    
    ans = max(ans,count)
print(ans)


