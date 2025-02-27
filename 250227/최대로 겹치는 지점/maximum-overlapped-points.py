n = int(input())
line = [0] * 110

for _ in range(n):
    x0,x1 = map(int,input().split())
    for i in range(x0,x1 + 1):
        line[i] += 1

print(max(line))