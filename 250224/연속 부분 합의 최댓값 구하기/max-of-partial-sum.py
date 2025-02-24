n = int(input())
arr = list(map(int, input().split()))

# Write your code here!


temp = 0
ans = min(arr)

for i in range(len(arr)):
    if arr[i] < 0:
        ans = max(ans,arr[i])
        temp = 0
    else:
        temp += arr[i]
        ans = max(ans,temp)
print(ans)
