n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
def check(n1,n2,n3):
    while True:
        if n1 == n2 == n3 == 0:
            break
        temp1,temp2,temp3 = n1 % 10,n2 % 10, n3 %10
        if (temp1+temp2+temp3) >= 10:
            return False
        n1,n2,n3 = n1//10,n2//10,n3//10
    return True

ans = -1

for i in range(n - 2):
    for j in range(i + 1,n - 1):
        for k in range(j + 1, n):
            n1,n2,n3 = arr[i],arr[j],arr[k]
            if check(n1,n2,n3):
                if n1 + n2 + n3 > ans:
                    ans = n1 + n2 + n3

print(ans)

