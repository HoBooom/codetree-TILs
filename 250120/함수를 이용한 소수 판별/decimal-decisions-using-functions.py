a, b = map(int, input().split())

# Write your code here!

def f(n):
    for j in range(2,n):
        if n % j == 0:
            #print(n)
            return False
    if n == 1:
        return False
    return True

ans = 0
for i in range(a, b + 1):
    if f(i):
        ans += i

print(ans)