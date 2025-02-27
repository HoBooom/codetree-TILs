n = int(input())

OFFSET = 10*100
MAXSET = 2*OFFSET + 1

commands = []

cnt = OFFSET

for _ in range(n):
    xi,dr = input().split()
    xi = int(xi)

    if dr == 'R':
        tempx1 = cnt
        tempx2 = cnt + xi
        commands.append((tempx1,tempx2))
        cnt = cnt + xi
    elif dr == 'L':
        tempx1 = cnt - xi
        tempx2 = cnt
        commands.append((tempx1,tempx2))
        cnt = cnt - xi

line=[0] * MAXSET

for _,item in enumerate(commands):
    for i in range(item[0],item[1]):
        line[i] += 1

ans = 0
for _,item in enumerate(line):
    if item >=2:
        ans += 1
print(ans)