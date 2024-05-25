n = int(input())

list0=[]

length=0
a = 0

for i in range(n):
    temp_list =input()
    if temp_list[0] == 'a':
        a += 1
    length += len(temp_list)

print(length, a)