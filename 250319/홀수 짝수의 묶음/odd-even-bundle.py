n = int(input())
nums = list(map(int,input().split()))

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

group_num = 0
while True:
    if group_num % 2 == 0:
        if even > 0:
            even -= 1
            group_num += 1
        elif odd >= 2:
            odd -= 2
            group_num += 1
        else:
            #현재 짝수 만들어야하는데 못 만듬
            #앞에가 홀수 집합
            if even > 0 or odd > 0:
                group_num -= 1
            break
    else:
        if odd > 0:
            odd -= 1
            group_num += 1
        else:
            break
print(group_num)

        



    