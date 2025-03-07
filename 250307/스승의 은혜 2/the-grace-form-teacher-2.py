n,budget = map(int,input().split())
price = [int(input()) for _ in range(n)]

price.sort()

ans = 0

for i in range(n):
    students_price = 0
    students = 0
    is_over = False
    for j in range(n):
        if j == i:
            students_price += (price[j]//2)
        else:
            students_price += price[j]
        if students_price <= budget:
            students += 1
        else:
            is_over = True
            break
    if ans < students:
        ans = students

print(ans)

