n = int(input())

nums = []

for i in range(1,9):
    for j in range(1,9):
        for k in range(1,9):
            if j != i:
                if k != i and k != j:
                    num = (i*100 + j*10 + k)
                    nums.append(list(str(num)))

def count1(num1,num2): #num1이 정답, num2가 체크
    count = 0
    for i in range(3):
        if num1[i] == num2[i]:
            count += 1
    return count

def count2(num1,num2):
    count = 0
    for i in range(3):
        if num1[i] != num2[i] and (num2[i] in num1):
            count += 1
    return count

for _ in range(n):
    num,c1,c2 = input().split()
    num = list(num)
    c1 = int(c1)
    c2 = int(c2)
    for i in range(len(nums)):
        if count1(nums[i],num) != c1 or count2(nums[i],num) !=c2:
            nums[i] = '000'

ans = 0

for _,item in enumerate(nums):
    if item != '000':
        #print(item)
        ans += 1

print(ans)
    




