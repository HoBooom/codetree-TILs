n, m = map(int, input().split())
A = list(map(int, input().split()))

# Write your code here!

A.insert(0,0)

ans = 0

while m >= 1:
    ans += A[m]
    if m % 2 == 0:
        m = m // 2
    else:
        m -= 1

print(ans)

