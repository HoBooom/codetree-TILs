#가장 가까운 두사람의 거리의 최댓값
#가장 멀리 떨어진 2명의 위치를 찾고
#그 가운데 위치에 사람을 넣은 후
#해당 배치의 가장 가까운 사람의 거리가 정답임
import sys
INT_MAX = sys.maxsize

n = int(input())
mans = list(input())

#print(mans)
max_x0 = max_x1 = 0
cnt_x0 = 0

max_dis = cnt_dis = 0
ans = INT_MAX

for i in range(1,n):
    if mans[i] == "1":
        if max_dis < cnt_dis:
            max_x0 = cnt_x0
            max_x1 = i
            max_dis = cnt_dis
        cnt_x0 = i
        cnt_dis = 0
    else:
        cnt_dis += 1
    

mans[(max_x0 + max_x1) // 2] = "1"

#print(mans)
cnt_dis2 = 0
for i in range(1,n):
    if mans[i] == "1":
        ans = min(ans,cnt_dis2)
        cnt_dis2 = 0
        # print(i)
    else:
        cnt_dis2 += 1
    # print(f"cnt_dis : {cnt_dis2}")
            
print(ans + 1)

