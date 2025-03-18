n = int(input())

cnt_point = [0,0,0]

alpha_to_num = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
}
num_to_alpha = ["A","B","C"]

def honor(points):
    max_n = max(cnt_point)
    people = []
    for i in range(3):
        if points[i] == max_n:
            people.append(num_to_alpha[i])
    return set(people)

before_honor = honor(cnt_point)

count = 0

for _ in range(n):
    stu, p = input().split()
    p = int(p)
    stu_num = alpha_to_num[stu]
    cnt_point[stu_num] += p
    cnt_honor = honor(cnt_point)
    if before_honor != cnt_honor:
        count += 1
    before_honor = cnt_honor

print(count)
