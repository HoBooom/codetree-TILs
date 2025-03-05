import sys

INT_MAX = sys.maxsize

n, m = map(int,input().split())

nums = list(map(int,input().split()))

blank = []

for i in range(n - 1):
    blank.append(nums[i])
    blank.append(0)
blank.append(nums[-1])

ans = INT_MAX

for i in range(n + (n - 2)):
    for j in range(i + 1, n + (n - 2)):
        #print(i,j)
        if i % 2 == 0 or j % 2 == 0:
            continue
        temp1 = (blank[:i])
        temp2 = (blank[i + 1:j])
        temp3 = (blank[j + 1:])
        temp = max(sum(temp1),sum(temp2),sum(temp3))
        #print(temp1,temp2,temp3)
        ans = min(ans,temp)


print(ans)

            
