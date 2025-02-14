N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Write your code here!
ans = 0
for i in range(N - M + 1):
    isBeutiful = True
    temp_list = A[i:i+M]
    temp_list.sort()
    B.sort()
    for j in range(M):
        if temp_list[j] != B[j]:
            isBeutiful = False
            break
    if isBeutiful:
        ans += 1
print(ans)
    
