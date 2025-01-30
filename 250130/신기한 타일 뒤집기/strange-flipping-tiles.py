n = int(input())

OFFSET = 1000*100
line = [0] * (2*OFFSET + 1)

cnt = OFFSET

for _ in range(n):
    xi,dr = input().split()
    if dr == 'R':
        for _ in range((int(xi))):
            line[cnt] = 1
            cnt += 1
        cnt -= 1
    elif dr == 'L':
        for _ in range((int(xi))):
            line[cnt] = 2
            cnt -= 1
        cnt += 1

w = 0
b = 0

for elem in line:
    if elem == 1:
        b += 1
    elif elem == 2:
        w += 1

print(w,b)