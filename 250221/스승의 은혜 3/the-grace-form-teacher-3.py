n,b = map(int,input().split())

stu = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    budget = 0
    students = 0
    new_list = []
    for j in range(n):
        if i == j:
            new_list.append(stu[j][0]//2 + stu[j][1])
        else:
            new_list.append(stu[j][0] + stu[j][1])
    #print(new_list)
    new_list.sort()
    #print(new_list)
    #print()
    
    
    for j in range(n):
        budget += (new_list[j])
        #print(budget,end = " ")
        if budget > b:
            break
        else:
            students += 1
    #print("stu",students)
    if ans <= students:
        ans = students
        #print(ans)

print(ans)
    
        