n = int(input())

hills = [int(input()) for _ in range(n)]

hills.sort()

cost = 0

def check(hill1,hill2):
    if 0 <= hill2 - hill1 <=17:
        return True
    return False 

def f(hill1,hill2):
    temp1 = hill1
    temp2 = hill2
    while True:
        if temp2 - temp1 <= 17:
            break
        temp1 += 1
        temp2 -= 1
    return temp1,temp2
    
length = n - 1

for i in range(length): 
    if check(hills[i], hills[length - i]):
        break
    t1,t2 = f(hills[i], hills[length - i])
    cost += ((t1 - hills[i]) ** 2) + ((hills[length - i] - t2) ** 2)

print(cost)

    
