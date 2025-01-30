n = int(input())
x = []
dir = []


# Write your code here!

line = [0] * (2*10*100 + 1)
cnt = 10 * 100

for _ in range(n):
    xi, di = input().split()
    xi = int(xi)
    if di == 'R':
        for i in range(xi):
            line[cnt] += 1
            cnt += 1
    if di =='L':
        for i in range(xi):
            line[cnt] += 1
            cnt -= 1

ans = 0
for idx,value in enumerate(line):
    if value >=2:
        ans+= 1
print(ans)