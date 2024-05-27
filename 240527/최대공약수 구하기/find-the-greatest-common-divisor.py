n,m = map(int,input().split())

ans = 1

if n > m:
    for i in range(2,m + 1):
        if n % i == 0 and m % i == 0:
            ans = i
else:
    for i in range(2,n + 1):
        if n % i == 0 and m % i == 0:
            ans = i

print(ans)