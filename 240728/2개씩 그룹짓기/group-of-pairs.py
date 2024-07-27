n = int(input())

arr = list(map(int,input().split()))

arr.sort()

temp =[]

for i in range(n):
    temp.append(arr[i] + arr[2*n - (1 + i)])

print(max(temp))