a, b = map(int, input().split())

# Write your code here!

def f(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def f1(n):
    temp = 0
    while n % 10 != 0:
        temp += n%10
        n = n // 10

    if temp % 2 == 0:
        return True
    else:
        return False

ans = 0

for i in range(a,b+1):
    if f(i) and f1(i):
        ans += 1

print(ans)