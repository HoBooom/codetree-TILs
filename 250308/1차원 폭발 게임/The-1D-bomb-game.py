n, m = map(int,input().split())

boom = [int(input()) for _ in range(n)]

def check(boom):
    count = 1
    for i in range(1,len(boom)):
        if boom[i] == boom[i - 1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
    return False

def set_boom(boom):
    count = 1
    start = 0
    end = 0
    for i in range(1,len(boom)):
        if boom[i] == boom[start]:
            count += 1
        elif boom[i] != boom[start]: #바뀜
            if count >= m:
                end = i
                for j in range(start,i):
                    boom[j] = 0
            start = i
            count = 1
        if i == len(boom) - 1:
            if count >= m:
                end = i + 1
                for j in range(start,end):
                    boom[j] = 0
        

while True:
    #print(*boom)
    if m == 1:
        boom = []
        break
    if not check(boom):
        break
    
    set_boom(boom)
    #print(*boom)
    temp = []
    for i in range(len(boom)):
        if boom[i] != 0:
            temp.append(boom[i])
    boom = temp

print(len(boom))
for i in range(len(boom)):
    print(boom[i])

