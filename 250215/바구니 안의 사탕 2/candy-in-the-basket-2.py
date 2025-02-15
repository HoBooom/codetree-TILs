N, K = map(int, input().split())
candy_box = [0] * 101

for _ in range(N):
    c, p = map(int, input().split())
    candy_box[p] = c

ans = 0


for i in range(len(candy_box)):
    first = i - K
    end = i + K
    if first < 0:
        first = 0
    if end > 100:
        end = 100
    temp = sum(candy_box[first:end + 1])
    if temp > ans:
        #print(first,end,temp)
        ans = temp

print(ans)
    
