n  = int(input())

nums = [
    int(input()) for _ in range(n)
]


nums.sort(reverse = True)
#print(nums)

ans = -1

def is_carry(num1,num2):
    while num1 > 0 and num2 > 0:
        
        n1 = num1 % 10
        n2 = num2 % 10
        if n1 + n2 >= 10:
            return True
        num1 //= 10
        num2 //= 10
    return False



for i in range(n - 2):
    temp = 0
    n1 = nums[i]
    for j in range(i + 1, n - 1):
        n2 = nums[j]
        #print("n1,n2: ",n1,n2)
        if is_carry(n1,n2) == False:
            temp = n1 + n2
            for k in range(j + 1,n):
                n3 = nums[k]
                #print("n1,n2,n3: ",n1,n2,n3)
                if is_carry(temp,n3) == False:
                    ans = temp + n3
                    break
        if ans != -1:
            break
    if ans != -1:
        break

print(ans)