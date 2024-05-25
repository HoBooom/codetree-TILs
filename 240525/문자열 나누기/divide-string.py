n= int(input())

integers = list(map(str,input().split()))

integer = ''.join(integers)

count = 0
for i in range(len(integer)):
    count += 1
    print(integer[i],end="")
    if count % 5 ==0:
        print()