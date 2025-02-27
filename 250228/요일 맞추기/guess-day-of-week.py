m1, d1, m2, d2 = map(int, input().split())

# Write your code here!

month31 = [1,3,5,7,8,10,12]
month30 = [4,6,9,11]

days = 0

if m1 < m2:
    while True:
        d1 += 1
        days += 1
        if m1 == m2 and d1 == d2:
            break
        if m1 in month30 and d1 == 30:
            m1 += 1
            d1 = 0
        elif m1 in month31 and d1 == 31:
            m1 += 1
            d1 = 0
        elif m1 == 2 and d1 == 28:
            m1 += 1
            d1 = 0
elif m1 > m2:
    while True:
        d2 += 1
        days -= 1
        if m1 == m2 and d1 == d2:
            break
        if m2 in month30 and d2 == 30:
            m2 += 1
            d2 = 0
        elif m2 in month31 and d2 == 31:
            m2 += 1
            d2 = 0
        elif m2 == 2 and d2 == 28:
            m2 += 1
            d2 = 0
else:
    if d1 > d2:
        while True:
            d2 += 1
            days -= 1
            if d1 == d2:
                break
    elif d1 < d2:
        while True:
            d1 += 1
            days += 1
            if d1 == d2:
                break

#0 1 2 3 4 5 6
day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

cnt = 0
#print(days)

if days < 0:
    for i in range(1, abs(days) + 1):
        cnt -= 1
        cnt = cnt % 7
else:
    for i in range(1, abs(days) + 1):
        cnt += 1
        cnt = cnt % 7

#print(cnt)
print(day[cnt])

