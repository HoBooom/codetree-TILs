n, t = map(int,input().split())

line1 = list(map(int,input().split()))
line2 = list(map(int,input().split()))

for time in range(t):
    temp1 = line1[-1]
    temp2 = line2[-1]
    for i in reversed(range(1,n)):
        line1[i] = line1[i - 1]
    for j in reversed(range(1,n)):
        line2[j] = line2[j - 1]
    line1[0] = temp2
    line2[0] = temp1

for i in range(n):
    print(line1[i], end = " ")
print()
for i in range(n):
    print(line2[i], end = " ")
    
