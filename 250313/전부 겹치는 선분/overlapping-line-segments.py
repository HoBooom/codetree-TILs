n = int(input())

line = [0] * 110

for _ in range(n):
    a1,a2 = map(int,input().split())
    for i in range(a1,a2 + 1):
        line[i] += 1

if max(line) == n:
    print("Yes")
else:
    print("No")
