import sys

INT_MAX = sys.maxsize

n = int(input())
chair = list(input())

def min_dis(chair):
    temp_min = INT_MAX

    idx_list = []
    for idx,item in enumerate(chair):
        if item == '1':
            idx_list.append(idx)
    
    for i in range(1,len(idx_list)):
        temp_min = min(temp_min,idx_list[i] - idx_list[i - 1])
    
    return temp_min

ans = 0

for i in range(len(chair)):
    for j in range(i + 1,len(chair)):
        temp_chair = chair[:]
        if chair[i] == '0' and chair[j] == '0':
            temp_chair[i] = temp_chair[j] = '1'
            ans = max(ans,min_dis(temp_chair))

print(ans)


