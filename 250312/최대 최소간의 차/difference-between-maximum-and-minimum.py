from collections import Counter
import sys

INT_MAX = sys.maxsize

n, k = map(int,input().split())

nums = list(map(int,input().split()))

nums_counter = Counter(nums)
ori_counter = nums_counter.copy()
#print(ori_counter)

ans = INT_MAX

def check_min_max(nums_counter):
    min_num = 10000
    min_num_count = 0
    max_num = 0
    max_num_count = 0
    for num, count in nums_counter.items():
        #print(num,count)
        if min_num > num:
            min_num = num
            min_num_count = count
        if max_num < num:
            max_num = num
            max_num_count = count
    return min_num,min_num_count,max_num,max_num_count

for cost in range(k + 1):
    nums_counter = ori_counter.copy()
    min_num,min_num_count,max_num,max_num_count = check_min_max(nums_counter)
    #print(cost)
    cnt_cost = 0
    #print(min_num,min_num_count,max_num,max_num_count)
    while max_num - min_num > cost:
        if min_num_count >= max_num_count:
            nums_counter[max_num - 1] = nums_counter.get(max_num - 1, 0) + nums_counter.pop(max_num)
            cnt_cost += max_num_count
        elif min_num_count < max_num_count:
            nums_counter[min_num + 1] = nums_counter.get(min_num + 1, 0) + nums_counter.pop(min_num)
            cnt_cost += min_num_count
        min_num,min_num_count,max_num,max_num_count = check_min_max(nums_counter)
        #print(min_num,min_num_count,max_num,max_num_count,"cost",cnt_cost)
    
    #print(cnt_cost)
    ans = min(cnt_cost,ans)
        
print(ans)

    
    

    