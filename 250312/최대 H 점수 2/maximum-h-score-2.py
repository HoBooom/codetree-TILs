from collections import Counter

N,L = map(int,input().split())

num_list = list(map(int,input().split()))

num_counter = Counter(num_list)

def bigger_than_num(cnt_num):
    count = 0
    for num,count_n in num_counter.items():
        if num >= cnt_num:
            count += count_n
    return count

def count_minus_one(cnt_num):
    count = 0
    for num,count_n in num_counter.items():
        if num == cnt_num - 1:
            count += count_n
            break
    return count


ans = 0

for cnt_num in range(1,100):
    count_sum = bigger_than_num(cnt_num)
    cnt_num_minus_one = count_minus_one(cnt_num - 1)

    if cnt_num_minus_one >= L:
        count_sum += L
    else:
        count_sum += cnt_num_minus_one
    
    if count_sum >= cnt_num:
        ans = max(ans,cnt_num)
    

print(ans)


        
    



    