n, k = map(int,input().split())

boom = [int(input()) for _ in range(n)]

max_count = -1
ans = 0

for i in range(n - k):
    temp = boom[i : i + k + 1]
    temp.sort()
    count = 1
    for j in range(1,len(temp)):
        if temp[j] == temp[j - 1]:
            count += 1
            if j == len(temp) - 1 and count >= 2:
                if count > max_count:
                    max_count = count
                    ans = temp[j - 1]
                elif count == max_count:
                    ans = max(ans,temp[j - 1])   
        else:
            if count >= 2:
                if count > max_count:
                    max_count = count
                    ans = temp[j - 1]
                elif count == max_count:
                    ans = max(ans,temp[j - 1])            
            count = 1

print(ans)

    


