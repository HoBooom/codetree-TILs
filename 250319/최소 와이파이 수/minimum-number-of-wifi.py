man,wifi = map(int,input().split())

mans = list(map(int,input().split()))

wifi_area = 2 * wifi + 1
ans = 0

temp_count = 0
for i in range(man):
    if mans[i] == 1 and temp_count == 0:
        ans += 1
        temp_count += 1
    elif temp_count >= 1:
        temp_count += 1

    if temp_count > wifi_area:
        if mans[i] == 1:
            ans += 1
            temp_count = 1
        else:
            temp_count = 0
    #print(f"idx : {i}, cnt_wifi_count : {ans}, temp_count : {temp_count}")
print(ans)



