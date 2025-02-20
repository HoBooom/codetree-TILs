import sys

MAXSIZE = sys.maxsize

#사람수, 치즈 수, 치즈 먹은 기록 수, 아픈 기록 수
n,m,d,s = map(int,input().split())


#d줄에 걸쳐 p몇번째 사람이, 몇 번째 치즈(m)을 언제(t) 먹었는지
datas = []
for _ in range(d):
    p,n_cheese,time = map(int,input().split())
    datas.append((p,n_cheese,time))

datas.sort(key = lambda x:(x[0],x[2]))


#s줄에걸쳐  몇번째 사람이 언제 확실히 아팠는지
#(아프다고 기록된 사람 외에도 아픈 사람 있었을 수 있음)
hospital = []
for _ in range(s):
    man,time = map(int,input().split())
    hospital.append((man,time))

def check_hospital(man):
    for i in range(len(hospital)):
        if hospital[i][0] == man:
            return hospital[i][1]
    return MAXSIZE

def is_sick(man):
    for i in range(len(hospital)):
        if hospital[i][0] == man:
            return True
    return False

def f(man,cheese):
    temp = check_hospital(man)
    is_eat = False
    for _,(p,c,t) in enumerate(datas):
        if p == man and cheese == c and t < temp:
            is_eat = True
    return is_eat

ans = 0

#i번 치즈가 상했다고 가정
for i in range(1,m + 1):
    is_contradiction = False

    probability = 0
    for _,(p,cheese,t) in enumerate(datas):
        if cheese == i and t < check_hospital(p):
            probability += 1
        elif cheese == i and t >= check_hospital(p):
            if not f(p,cheese):
                is_contradiction = True
    
    for man in range(1,n + 1):
        if is_sick(man):
            eat = False
            for _,(p,cheese,t) in enumerate(datas):
                if cheese == i:
                    eat = True
            if not eat:
                is_contradiction = True

    if is_contradiction:
        continue
    if ans < probability:
        ans = probability


print(ans)