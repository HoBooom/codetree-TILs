list0=[]



for i in range(2):
    temp_list = list(map(int,input().split()))
    list0.append(temp_list)

for i in range(2):
    print(sum(list0[i])/4,end=" ")
print()

for j in range(4):
    column_avg=(list0[0][j] + list0[1][j]) / 2
    print(column_avg,end=" ")
print()

sum1=sum(list0[0])
sum2=sum(list0[1])
all_avg = ((sum1+sum2)/8)

print(round(all_avg,1))