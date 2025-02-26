n, k = map(int,input().split())

block = [0] * (n + 1) 

for _ in range(k):
    x0,x1 = map(int,input().split())
    for i in range(x0,x1 + 1):
        block[i] += 1

print(max(block))