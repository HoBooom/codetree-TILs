n = int(input())

n1,n2,n3 = map(int,input().split())

count = 0 



for i in range(1,n + 1):
    for j in range(1,n + 1):
        for k in range(1,n + 1):
            if  (n1 - 2 <= i <= n1 + 2) or (n2 - 2 <= j <= n2 + 2) or (n3 - 2 <= k <= n3 + 2):
                count += 1

print(count)