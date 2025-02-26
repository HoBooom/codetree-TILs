n = int(input())


# Please write your code here.

line = [0] * 201

for _ in range(n):
    x0,x1 = map(int,input().split())
    x0,x1 = x0 + 100, x1 + 100
    for i in range(x0,x1):
        line[i] += 1

print(max(line))