n = int(input())
people = ['0']* 101

for _ in range(n):
    pos,alpha = input().split()
    pos = int(pos)
    people[pos] = alpha


def check(start,end):
    count_G = 0
    count_H = 0

    for i in range(start,end + 1):
        if people[i] == 'G':
            count_G += 1
        elif people[i] == 'H':
            count_H += 1
    if count_H !=0 and count_G == count_H:
        return True
    elif count_G == 0 and count_H != 0:
        return True
    elif count_G != 0 and count_H == 0:
        return True
    return False

ans = 0

for i in range(len(people)):
    for j in range(i,len(people)):
        if people[i] == '0' or people[j] == '0':
            continue
        if check(i,j):
            #print(j,i)
            temp = j - i
            if temp > ans:
                ans = temp

print(ans)



