size=int(input())

items=list(map(int,input().split()))

for i in range(size):
    min = items[i]
    for j in range(i,size):
        if min > items[j]:
            items[i],items[j] = items[j],items[i]
        min = items[i]

for i in range(size):
    print(items[i],end=" ")