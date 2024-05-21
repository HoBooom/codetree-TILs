n,m = map(int,input().split())

list1 = []
list2 = []


for i in range(n):
    temp_list =list(map(int,input().split()))
    list1.append(temp_list)

for i in range(n):
    temp_list =list(map(int,input().split()))
    list2.append(temp_list)

list0 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if list1[i][j] == list2[i][j]:
            list0[i][j] =0
        else:
            list0[i][j] = 1

for i in range(n):
    for j in range(m):
        print(list0[i][j],end=" ")
    print()