n = int(input())

arr = list(map(int,input().split()))

temp = []

for i,v in enumerate(arr):
    temp.append(v)
    if i % 2 == 0:
        temp.sort()
        print(temp[len(temp)//2],end=" ")