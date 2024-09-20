n = int(input())

mans = []

for _ in range(n):
    place,alpha = map(str,input().split())
    mans.append((int(place),alpha))

mans.sort(key = lambda x: x[0])


ans = 0

for i in range(n):
    g_count = 0
    h_count = 0

    for j in range(i,n):
        temp = 0

        if mans[j][1] == 'G':
            g_count += 1
        else:
            h_count += 1

        if (g_count != 0 and h_count == 0) or (g_count == 0 and h_count != 0) or (g_count == h_count):
            temp = mans[j][0] - mans[i][0]
            ans = max(ans,temp)

print(ans)