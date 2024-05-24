row = int(input())

list0=[]

for i in range(1,row + 1):
    temp_list = [1 for _ in range(i)]
    list0.append(temp_list)

for i in range(row):
    for j in range(1,len(list0[i])):
        if list0[i - 1][j - 1] and j < i:
            list0[i][j] = list0[i - 1][j - 1] + list0[i - 1][j]


for i in range(row):
    for j in range(len(list0[i])):
        print(list0[i][j],end=" ")
    print()