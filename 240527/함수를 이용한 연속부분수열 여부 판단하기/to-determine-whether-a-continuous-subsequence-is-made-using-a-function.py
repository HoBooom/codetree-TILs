def is_part(list0,list1,index):
    for i in range(len(list1)):
        if list1[i] != list0[index + i]:
            return False
    return True



n,m = map(int,input().split())

list0 = list(map(int,input().split()))
list1 = list(map(int,input().split()))

tf = False

for i in range(n-m+1):
    if list0[i]==list1[0]:
        tf = is_part(list0,list1,i)
        if tf:
            break

if tf:
    print("Yes")
else:
    print("No")