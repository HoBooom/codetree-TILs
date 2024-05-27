c = 1

n = int(input())

for i in range(n):
    for j in range(n):
        print(c,end=" ")
        if c == 9:
            c = 1
        else:
            c+=1
    print()