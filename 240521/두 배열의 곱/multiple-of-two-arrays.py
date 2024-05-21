list0 = []
list1 = []

for i in range(3):
    temp_list = list(map(int, input().split()))
    list0.append(temp_list)

blank = input()

for j in range(3):
    temp_list = list(map(int, input().split()))
    list1.append(temp_list)


list2 = []

for i in range(3):
    temp_row =[]
    for j in range(3):
        
        temp = list0[i][j] * list1[i][j]
        temp_row.append(temp)
    list2.append(temp_row)

for i in range(3):
    for j in range(3):
        print(list2[i][j], end=" ")
    print()