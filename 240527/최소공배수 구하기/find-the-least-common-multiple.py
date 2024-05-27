def min_mul(n,m):
    ans = 1

    if n>m:
        for i in range(2,m+ 1):
            if n % i ==0 and m % i == 0:
                ans = i
    else:
        for i in range(2,n + 1):
            if n % i ==0 and m % i == 0:
                ans = i
    return ans


def max_mul(n,m):
    temp_min = min_mul(n,m)
    return abs(n*m) / temp_min

n,m = map(int,input().split())

ans = max_mul(n,m)

print(int(ans))