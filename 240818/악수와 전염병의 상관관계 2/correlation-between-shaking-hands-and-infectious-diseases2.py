n,k,p,t = map(int,input().split())
# n명
# k번 악수동안 전염병을 옮김
# p - 개발자 번호
# T초에 x개발자와 y개발자 악수


command = []
mans = [[False,0] for _ in range(n + 1)] #(전염여부, 남은 전염성)
mans[p] = [True,k] #초기 감염자 세팅

for _ in range(t):
    time,x,y = map(int,input().split())
    command.append((time,x,y))

command.sort(key = lambda x: x[0])
#print(command)

for i,v in enumerate(command):
    if mans[v[1]][0] == True and mans[v[2]][0] == False: #경우1 T,F
        #감염이 되었지만 감염성이 없음
        if mans[v[1]][1] == 0:
            continue
        else: #감염성이 있음
            mans[v[1]][1] -= 1 #x의 감염가능 - 1
            #y는 새로 감염됨
            mans[v[2]][0] = True
            mans[v[2]][1] = k
    elif mans[v[1]][0] == False and mans[v[2]][0] == True: #경우2 F,T
        #감염이 되었지만 감염성이 없음
        if mans[v[2]][1] == 0:
            continue
        else: #감염성이 있음
            mans[v[2]][1] -= 1 #y의 감염가능 - 1
            #x는 새로 감염됨
            mans[v[1]][0] = True
            mans[v[1]][1] = k
    elif mans[v[1]][0] == True and mans[v[2]][0] == True: #경우3 T,T
        if mans[v[1]][1] > 0:
            mans[v[1]][1] -= 1
        if mans[v[2]][1] > 0:
            mans[v[2]][1] -= 1
    elif mans[v[1]][0] == False and mans[v[2]][0] == False: #경우4 F,F
        continue

#print(mans)
for i in range(1,n + 1):
    print(int(mans[i][0]),end="")