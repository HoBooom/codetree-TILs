n = int(input())

ice = [int(input()) for _ in range(n)]

ans = 0

for k in range(max(ice)):
    count = 0
    ori_state = False
    for i in range(n):
        ice[i] -= k
    
    for i in range(n):
        cnt_state = False
        if ice[i] > 0:
            cnt_state = True
        if ori_state == False and cnt_state == True:
            count += 1
        ori_state = cnt_state

    ans = max(ans,count)
    for i in range(n):
        ice[i] += k

print(ans)