n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

ans = min(arr)

for i in range(len(arr)):
    temp = 0
    for j in range(i,len(arr)):
        temp += arr[j]
        ans = max(ans,temp)

print(ans)
