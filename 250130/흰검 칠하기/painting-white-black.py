n = int(input())

OFFSET = 1000*100
MAXSET = 2*OFFSET + 1

line = [['0'] for _ in range(MAXSET)]
cnt = OFFSET

for _ in range(n):
    xi, dr = input().split()
    if dr == 'R':
        for _ in range(int(xi)):
            line[cnt].append('B')
            cnt += 1
        cnt -= 1
    if dr == 'L':
        for _ in range(int(xi)):
            line[cnt].append('W')
            cnt -= 1
        cnt += 1

black = 0
gray = 0
white = 0

for elem in line:
    b = 0
    w = 0
    for _,item in enumerate(elem):
        if item =='B':
            b += 1
        elif item == 'W':
            w += 1
    
    if b >= 2 and w>=2:
        gray += 1
    elif elem[len(elem) - 1] == 'B':
        black +=1
    elif elem[len(elem) - 1] == 'W':
        white += 1

print(white,black,gray)


