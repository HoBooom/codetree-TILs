temp = []


for i in range(4):
    sum = 0
    list1=list(map(int,input().split()))
    temp.append(list1)
    for j in range(4):
        sum += list1[j]
    print(sum)