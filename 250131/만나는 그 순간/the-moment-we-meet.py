n,m = map(int,input().split())


a = []
b = []
a.append(0)
b.append(0)

cnt_a = 0
cnt_b = 0

for _ in range(n):
    dr,xa = input().split()
    xa= int(xa)
    if dr == 'R':
        for _ in range(xa):
            cnt_a += 1
            a.append(cnt_a)
    elif dr =='L':
        for _ in range(xa):
            cnt_a -= 1
            a.append(cnt_a)

for _ in range(m):
    dr,xb = input().split()
    xb = int(xb)
    if dr =='R':
        for _ in range(xb):
            cnt_b += 1
            b.append(cnt_b)
    elif dr =='L':
        for _ in range(xb):
            cnt_b -= 1
            b.append(cnt_b)

#print(a)
#print(b)
isTrue = False

for i,item in enumerate(a):
    if item == b[i] and i != 0:
        print(i)
        isTrue = True
        break
            
if not isTrue:
    print(-1)
    