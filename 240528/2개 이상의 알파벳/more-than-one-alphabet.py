a= input()

list0 = []

for i in range(len(a)):
    ascii = ord(a[i])
    if ascii not in list0:
        list0.append(ascii)

if len(list0) > 1:
    print("Yes")
else:
    print("No")