n,m = map(int,input().split())

nums_a = list(map(int,input().split()))
nums_b = list(map(int,input().split()))

def is_in_list(temp_list,check_b):
    

    for i in range(len(temp_list)):
        if temp_list[i] not in nums_b:
            return False

        for i,v in enumerate(check_b):
            if v[0] == temp_list[i] and v[1] == False:
                v[1] = True
                break
        
    for i,v in enumerate(check_b):
        if v[1] == False:
            return False

    return True

count = 0

check_b = []
for i in range(m):
    check_b.append([nums_b[i],False])
#print(check_b)


for i in range(n - m + 1):
    temp_list = nums_a[i:i + m]
    
    
    if is_in_list(temp_list,check_b):
        count += 1

print(count)