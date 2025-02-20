n,b = map(int,input().split())

stu = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    budget = 0
    temp = stu[:]
    temp[i][0] = temp[i][0]//2
    temp.sort(key = lambda x:x[0])
    #print(temp)
    students = 0
    for j in range(n):
        budget += (temp[j][0] + temp[j][1])
        if budget > b:
            budget -= (temp[j][0] + temp[j][1])
        else:
            students += 1
    if students > ans:
        ans = students

print(students)
    
        