n = int(input())

arr =[]

for _ in range(n):
    temp = input()
    arr.append(temp)

arr.sort()

for i,v in enumerate(arr):
    print(v)