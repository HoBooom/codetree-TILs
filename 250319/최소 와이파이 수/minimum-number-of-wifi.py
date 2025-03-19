man,wifi = map(int,input().split())

mans = list(map(int,input().split()))

wifi_area = 2 * wifi + 1
ans = cnt_idx = 0

while cnt_idx < man:
    if mans[cnt_idx] == 1:
        ans += 1
        cnt_idx += wifi_area
    else:
        cnt_idx += 1

print(ans)



