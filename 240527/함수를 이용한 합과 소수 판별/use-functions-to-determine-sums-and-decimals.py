def is_sosu(n):
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

def is_2_mul(n):
    temp = str(n)
    sum0=0
    for i in range(len(temp)):
        sum0 += int(temp[i])
    if sum0 % 2==0 and sum0 != 0:
        return True
    return False

n,m = map(int,input().split())

count = 0

for i in range(n,m+ 1):
    if is_2_mul(i) and is_sosu(i):
        count +=1
print(count)