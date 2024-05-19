list0=[]

for i in range(5):
    list_temp =list(map(str,input().split()))
    for j in range(3):
        list_temp[j]= list_temp[j].upper()
    list0.append(list_temp)


for index,value in enumerate(list0):
    for j in range(3):
        print(value[j],end=" ")
    print()