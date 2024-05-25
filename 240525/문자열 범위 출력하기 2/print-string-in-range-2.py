arr = input()
n = int(input())

for i in range(1,n+1):
    temp = -1 * i
    if len(arr) >= i:
        print(arr[temp],end ="")