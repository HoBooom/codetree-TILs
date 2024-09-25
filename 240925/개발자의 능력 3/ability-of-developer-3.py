import sys

INTMAX = sys.maxsize

mans = list(map(int,input().split()))

def f(i,j,k):
    sum1 = mans[i] + mans[j] + mans[k]
    sum2 = sum(mans) - sum1

    return abs(sum1 - sum2)


ans  = INTMAX
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1,6):
            ans = min(ans,f(i,j,k))
print(ans)