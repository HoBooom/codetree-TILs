size=int(input())

items=list(map(int,input().split()))

for i in range(1,size):
    key= items[i]
    j = i -1
    while j >= 0 and items[j] > key:
        items[j + 1] = items[j]
        j -= 1
    items[j + 1]=key 

for i in range(size):
    print(items[i],end=" ")