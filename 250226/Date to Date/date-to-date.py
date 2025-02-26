m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

m_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

ans = 1

while True:
    if m1 == m2 and d1 == d2:
        break
    
    d1 += 1
    ans += 1

    if d1 > m_days[m1]:
        d1 = 1
        m1 += 1

print(ans)
