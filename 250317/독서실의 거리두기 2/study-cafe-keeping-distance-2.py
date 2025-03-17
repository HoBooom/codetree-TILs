import sys

INT_MAX = sys.maxsize

n = int(input())

place = list(input())

def min_dis(place):
    temp_distance = 1
    min_dis = INT_MAX
    
    cnt_start = -1
    for i in range(n):
        if place[i] == "1":
            if cnt_start == -1:
                cnt_start = i
                temp_distance = 1
                continue
            min_dis = min(min_dis,temp_distance)
            temp_distance = 1
        else:
            temp_distance += 1
    return min_dis

ans = 0
        
for i in range(n):
    if place[i] == "0":
        place[i] = "1"
        cnt_dis = min_dis(place) 
        ans = max(ans,cnt_dis)
        #print(place, cnt_dis)
        place[i] = "0"

print(ans)
    
