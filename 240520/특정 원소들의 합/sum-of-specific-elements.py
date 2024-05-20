list0 = []

for i in range(4):
    temp_list = list(map(int,input().split()))
    list0.append(temp_list)


sum = 0

for i in range(4):
    for j in range(4):
        if i >= j:
            sum += list0[i][j]

print(sum)