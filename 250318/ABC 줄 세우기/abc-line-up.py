n = int(input())

mans = list(map(str,input().split()))

count = 0

for i in range(n):
    cnt_alpha = mans[i]
    cnt_alpha_num = ord(cnt_alpha) - 65
    #print(cnt_alpha,cnt_alpha_num)
    if cnt_alpha_num == i:
        continue
    else:
        if cnt_alpha_num < i:
            mans = mans[:cnt_alpha_num] + [cnt_alpha] + mans[cnt_alpha_num:i] + mans[i + 1:]
        elif cnt_alpha_num > i:
            mans = mans[:i] + mans[i + 1:cnt_alpha_num + 1] + [cnt_alpha] + mans[cnt_alpha_num + 1:]
        count += abs(i - cnt_alpha_num)

print(count)