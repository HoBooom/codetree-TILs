n,k = map(int,input().split())

line = [0]*10001

for _ in range(n):
    pos, alpha = input().split()
    if alpha == 'G':
        line[int(pos)] = 1
    else:
        line[int(pos)] = 2

ans = 0

for i in range(10001 - k):
    temp = sum(line[i:i+k+1])
    ans = max(ans,temp)

print(ans)

