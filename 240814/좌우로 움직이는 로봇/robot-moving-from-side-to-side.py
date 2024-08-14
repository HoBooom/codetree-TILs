n,m = map(int,input().split())

a = []
b = []
time_a = 0
time_b = 0
a.append(0)
b.append(0)

cnt = 0
for _ in range(n):
    t,d = tuple(input().split())
    t = int(t)

    if d == "L":
        for i in range(1,t + 1):
            a.append(cnt - i)
        cnt -= t
        time_a += 1
    elif d == "R":
        for i in range(1,t + 1):
            a.append(cnt + i)
        cnt += t
        time_a += 1

cnt = 0
for _ in range(m):
    t,d = tuple(input().split())
    t = int(t)

    if d == "L":
        for i in range(1,t + 1):
            b.append(cnt - i)
        cnt -= t
        time_b += 1
    elif d == "R":
        for i in range(1,t + 1):
            b.append(cnt + i)
        cnt += t
        time_b += 1

cnt_a = 1
cnt_b = 1
count = 0

while True:
    if a[cnt_a] == b[cnt_b]:
        if cnt_a != 1 and (a[cnt_a - 1] != b[cnt_b - 1]):
            count += 1
        elif cnt_a == 1:
            count += 1
    if cnt_a + 1 < len(a): #a배열의 길이가 5이면 인덱스는 4까지만 커져야함
        cnt_a += 1
    if cnt_b + 1 < len(b):
        cnt_b += 1
    
    if cnt_a + 1 == len(a) and cnt_b + 1 == len(b):
        break

print(count)